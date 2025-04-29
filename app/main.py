import numpy as np

arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# print(arr * 2)
# print(matrix * 2)
# Output: [ 2  4  6  8 10]
#         [
#          [ 2  4  6]
#          [ 8 10 12]
#          [14 16 18]
#         ]



# zeros - 0
zeros = np.zeros((3, 4))
# print(zeros)
# Output:
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]



# ones - 1
ones = np.ones((2, 3))
# print(ones)
# Output:
# [[1. 1. 1.]
#  [1. 1. 1.]]


# One matrix
eye = np.eye(4)
# print(eye)
# Output:
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]


linspace = np.linspace(0, 10, 5)
# print(linspace)
# Output:
# [ 0.   2.5  5.   7.5 10. ]


arange = np.arange(0, 10, 3)
print(arange)
# Output:
# [0 3 6 9]