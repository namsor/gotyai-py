from operator import itemgetter
from bisect import bisect_right

import numpy as np
import pandas as pd


class Discretizer(object):

    def __init__(self, upperlim=20, bottomlim=0, mapping=False):
        self.mapping = mapping
        self.set_lims(upperlim, bottomlim)

    @property
    def cutoffs(self):
        return [i[0] for i in self.mapping]

    def set_lims(self, upperlim, bottomlim):
        if not self.mapping:
            self.bottomlim = bottomlim
            self.upperlim = upperlim
        else:
            vals = sorted(np.unique(map(itemgetter(1), self.mapping)))
            self.bottomlim = vals[0]
            self.upperlim = vals[-1]
        assert self.bottomlim < self.upperlim

    def fit(self, continuous_series, subsample=None):
        self.mapping = []
        continuous_series = pd.Series(continuous_series).reset_index(drop=True).dropna()
        if subsample is not None:
            n = len(continuous_series)*subsample if subsample < 1 else subsample
            continuous_series = np.random.choice(continuous_series, n, replace=False)
        ranked = pd.Series(continuous_series).rank(pct=1, method='average')
        ranked *= self.upperlim - self.bottomlim
        ranked += self.bottomlim
        ranked = ranked.map(round)
        nvals = sorted(np.unique(ranked))  # sorted in case numpy changes
        for nval in nvals:
            cond = ranked == nval
            self.mapping.append((continuous_series[cond].min(), int(nval)))

    def transform_single(self, val):
        if not self.mapping:
            raise NotImplementedError('Haven\'t been fitted yet')
        elif pd.isnull(val):
            return None
        i = bisect_right(self.cutoffs, val) - 1
        if i == -1:
            return 0
        return self.mapping[i][1]

    def transform(self, vals):
        if isinstance(vals, float):
            return self.transform_single(vals)
        elif vals is None:
            return None
        return pd.Series(vals).map(self.transform_single)

    def fit_transform(self, vals):
        self.fit(vals)
        return self.transform(vals)