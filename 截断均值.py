import numpy as np
from pandas import DataFrame as df
from scipy.stats import trim_mean, kurtosis
from scipy.stats.mstats import mode, gmean, hmean

N = 20
P = ["noise", "quiet"]
Q = [1, 2, 3]

values = [[998, 511], [1119, 620], [1300, 790]]

mus = np.concatenate([np.repeat(value, N) for value in values])

data = df(data={'id': [subid for subid in range(N)] * (len(P) * len(Q))
    , 'iv1': np.concatenate([np.array([p] * N) for p in P] * len(Q))
    , 'iv2': np.concatenate([np.array([q] * (N * len(P))) for q in Q])
    , 'rt': np.random.normal(mus, scale=112.0, size=N * len(P) * len(Q))})
grouped_data = data.groupby(['iv1', 'iv2'])
grouped_data['rt'].describe().unstack()
trimmed_mean = grouped_data['rt'].apply(trim_mean, .1)
trimmed_mean.reset_index()
print(trimmed_mean)