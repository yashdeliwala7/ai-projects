import numpy as np

arr = np.array([1, 2, 3, 4,"yash"])
print(arr)
print(arr.shape)
print(arr.dtype)

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr2)
print(arr2.shape)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a * b)