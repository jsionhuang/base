import numpy as np

# 2-D array:2*3
a = np.array([[1,2,3],[4,5,6]])
# 2-D array: 3*2
b = np.array([[1,2],[3,4],[5,6]])
multiply_result = np.dot(a,b)
print(multiply_result)