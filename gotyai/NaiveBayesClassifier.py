import numpy as np
import pandas as pd

class NaiveBayesClassifier(object):

    def __init__(self, alpha=1.0, class_priors=None, **kwargs):
        self.alpha = alpha
        self.class_priors = class_priors

    def get_class_log_priors(self, y):
        self.classes_ = y.unique()
        if self.class_priors is None:
            self.class_priors = y.value_counts(normalize=1)
        elif isinstance(self.class_priors, str) and self.class_priors == 'equal':
            raise NotImplementedError
        self.class_log_priors = self.class_priors.map(np.log)

    def get_log_likelihoods(self, fld):
        table = self.groups[fld].value_counts(dropna=False).unstack(fill_value=0)
        table += self.alpha
        sums = table.sum(axis=1)
        likelihoods = table.apply(lambda r: r/sums, axis=0)
        log_likelihoods = likelihoods.applymap(np.log)
        return {k if pd.notnull(k) else None: v for k, v in log_likelihoods.items()}

    def fit(self, X, y):
        y = pd.Series(y)
        self.get_class_log_priors(y)
        self.groups = X.groupby(y)
        self.log_likelihoods = {
            fld: self.get_log_likelihoods(fld)
            for fld, series in X.items()
        }

    def get_approx_log_posterior(self, series, class_):
        log_posterior = self.class_log_priors[class_]  # prior
        for fld, val in series.items():
            # there are cases where the `val` is not seen before
            # as in having a `nan` in the scoring dataset,
            #   but no `nans in the training set
            # in those cases, we want to not add anything to the log_posterior

            # This is to handle the Nones and np.nans etc.
            val = val if pd.notnull(val) else None

            if val not in self.log_likelihoods[fld]:
                continue
            log_posterior += self.log_likelihoods[fld][val][class_]
        return log_posterior

    def decision_function_series(self, series):
        approx_log_posteriors = [
            self.get_approx_log_posterior(series, class_)
            for class_ in self.classes_]
        return pd.Series(approx_log_posteriors, index=self.classes_)

    def decision_function_df(self, df):
        return df.apply(self.decision_function_series, axis=1)

    def decision_function(self, X):
        """
        returns the log posteriors
        """
        if isinstance(X, pd.DataFrame):
            return self.decision_function_df(X)
        elif isinstance(X, pd.Series):
            return self.decision_function_series(X)
        elif isinstance(X, dict):
            return self.decision_function_series(pd.Series(X))

    def predict_proba(self, X, normalize=True):
        """
        returns the (normalized) posterior probability

        normalization is just division by the evidence. doesn't change the argmax.
        """
        log_post = self.decision_function(X)
        if isinstance(log_post, pd.Series):
            post = log_post.map(np.exp)
        elif isinstance(log_post, pd.DataFrame):
            post = log_post.applymap(np.exp)
        else:
            raise NotImplementedError('type of X is "{}"'.format(type(X)))
        if normalize:
            if isinstance(post, pd.Series):
                post /= post.sum()
            elif isinstance(post, pd.DataFrame):
                post = post.div(post.sum(axis=1), axis=0)
        return post

    def predict(self, X):
        probas = self.decision_function(X)
        if isinstance(probas, pd.Series):
            return np.argmax(probas)
        return probas.apply(np.argmax, axis=1)

    def score(self, X, y):
        preds = self.predict(X)
        return np.mean(np.array(y) == preds.values)