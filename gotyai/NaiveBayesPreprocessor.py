from gotyai.Discretizer import Discretizer
import pandas as pd
import numpy as np
from collections import defaultdict
class NaiveBayesPreprocessor(object):
    """
    Don't pass in Nans. fill with keyword.
    """

    OTHER = '____OTHER____'
    FILLNA = '____NA____'

    def __init__(self, alpha=1.0, min_freq=0.01, bins=20):
        self.alpha = alpha  # Laplace smoothing
        self.min_freq = min_freq  # drop values occuring less frequently than this
        self.bins = bins  # number of bins for continuous fields

    def learn_continuous_transf(self, series):
        D = Discretizer(upperlim=self.bins)
        D.fit(series)
        return D

    def learn_discrete_transf(self, series):
        vcs = series.value_counts(dropna=False, normalize=True)
        vcs = vcs[vcs >= self.min_freq]
        keep = set(vcs.index)
        transf = lambda r: r if r in keep else self.OTHER
        return transf

    def learn_transf(self, series):
        if series.dtype == np.float64:
            return self.learn_continuous_transf(series)
        else:
            return self.learn_discrete_transf(series)

    def fit(self, X_orig, y=None):
        """
        Expects pandas series and pandas DataFrame
        """
        # get dtypes
        self.dtypes = defaultdict(set)
        for fld, dtype in X_orig.dtypes.iteritems():
            self.dtypes[dtype].add(fld)

        X = X_orig
        # X = X_orig.fillna(self.FILLNA)
        # get transfs
        self.transformations = {
            fld: self.learn_transf(series)
            for fld, series in X.iteritems()}

    def transform(self, X_orig, y=None):
        """
        Expects pandas series and pandas DataFrame
        """
        X = X_orig.copy()
        # X = X_orig.fillna(self.FILLNA)
        for fld, func in self.transformations.items():
            if isinstance(func, Discretizer):
                X[fld] = func.transform(X[fld])
            else:
                X[fld] = X[fld].map(func)
        return X

    def fit_transform(self, X, y=None):
        self.fit(X)
        return self.transform(X)