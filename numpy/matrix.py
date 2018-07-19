import numpy as np

# 2维矩阵 array:2*3
a = np.array([[1,2,3],[4,5,6]])
# 2 矩阵: 3*2
b = np.array([[1,2],[3,4],[5,6]])
multiply_result = np.dot(a,b)
print(multiply_result)

# 1维矩阵 array
a = np.array([1,2,3])
b = np.array([4,5,6])
multiply_result = np.dot(a,b)
print(multiply_result)