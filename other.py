import pandas as pd
from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import roc_auc_score
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from collections import defaultdict
from sklearn.pipeline import Pipeline
from gotyai.NaiveBayesClassifier import NaiveBayesClassifier
from gotyai.Discretizer import Discretizer
from gotyai.NaiveBayesPreprocessor import NaiveBayesPreprocessor
winedata = pd.read_csv('./datasets/Wine_Quality_Data.csv')
print(winedata.shape)
print('-'*30)
print(winedata.color.value_counts(normalize=True))
winedata.sample(3)

pipe = [('preprocessor', NaiveBayesPreprocessor(bins=20)),
        ('nb', NaiveBayesClassifier())]
pipe = Pipeline(pipe)
nbs = {'_vanilla_': pipe,
       'Multinomial': MultinomialNB(),
       'Bernoulli': BernoulliNB(),
       'Gaussian': GaussianNB()}

X, y = winedata[winedata.columns[:-1]], winedata[winedata.columns[-1]]

rs = ShuffleSplit(test_size=0.25, n_splits=5)
scores = defaultdict(list)
for train_index, test_index in rs.split(X):
    X_train, X_test = X.loc[train_index], X.loc[test_index]
    y_train, y_test = y.loc[train_index], y.loc[test_index]
    for key, est in nbs.items():
        est.fit(X_train, y_train)
        scores[key].append(est.score(X_test, y_test))

print(pd.DataFrame(scores))