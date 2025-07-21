import numpy as np

a = np.array([1, 2, 3])             # 1D array
b = np.array([[1, 2], [3, 4]])      # 2D array

np.zeros((2, 3))                    # 2x3 array of zeros
np.ones((3, 2))                     # 3x2 array of ones
np.eye(3)                           # 3x3 identity matrix
np.full((2, 2), 7)                  # 2x2 filled with 7
np.arange(0, 10, 2)                 # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)                # 5 values between 0 and 1

#Array atributes
arr = np.array([[1, 2], [3, 4]])

arr.shape      # (2, 2)
arr.ndim       # 2
arr.size       # 4
arr.dtype      # data type (e.g., int64)

#Indexing and slicing
arr = np.array([[1, 2, 3], [4, 5, 6]])

arr[0, 1]           # 2
arr[:, 1]           # [2, 5] (all rows, column 1)
arr[1, :]           # [4, 5, 6] (row 1)

#Mathematical operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b               # [5 7 9]
a * b               # [4 10 18] (element-wise)
np.dot(a, b)        # 32 (dot product)

np.mean(a)          # 2.0
np.std(b)           # Standard deviation
np.sum(a)           # 6
np.max(b)           # 6

#Reshaping and flattening
arr = np.array([[1, 2], [3, 4]])

arr.reshape(4, 1)

#Broadcasting (Allows arithmetic between arrays of different shapes:)
a = np.array([[1], [2], [3]])
b = np.array([10, 20, 30])
a + b

