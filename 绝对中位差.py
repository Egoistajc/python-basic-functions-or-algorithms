import numpy as np
def mad(arr):
    arr = np.ma.array(arr).compressed()  # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))

arr=[1,2,3,4,5,6,7,8,9]
print(mad(arr))