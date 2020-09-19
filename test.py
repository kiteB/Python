import numpy as np
array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
array1 > 6 # array([False, False, False,  True,  True,  True,  True,  True,  True, True,  True])
array1 % 2 == 0 # array([ True, False, False, False, False, False, False, False, False, False, False])

booleans = np.array([True, True, False, True, False, True, True, True, False, True])
np.where(booleans)  # (array([0, 1, 3, 5, 6, 7, 9], dtype=int64),)  (True인 값의 인덱스)
array1 > 4  # array([False, False,  True,  True,  True,  True,  True,  True,  True, True,  True])

np.where(array1 > 4)    # (array([ 2,  3,  4,  5,  6,  7,  8,  9, 10], dtype=int64),)

filter = np.where(array1 > 4)   # (array([ 2,  3,  4,  5,  6,  7,  8,  9, 10], dtype=int64),)
array1[filter]  # array([ 5,  7, 11, 13, 17, 19, 23, 29, 31])



