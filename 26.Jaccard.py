import numpy as np
import scipy.spatial.distance as dist

v1 = np.array([1, 1, 0, 1, 0, 1, 0, 0, 1])
v2 = np.array([0, 1, 1, 0, 0, 0, 1, 1, 1])
v3 = np.array([0, 1, 0, 0, 0, 0, 0, 1, 1])

matv = np.array([v1, v2, v3])
print(matv)
ds = dist.pdist(matv, 'jaccard')
print(ds)

