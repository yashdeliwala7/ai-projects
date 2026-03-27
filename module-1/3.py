import numpy as np

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])

arr2=np.array([[1,2,3,4,5,6,7,8,9],[1,2],[5,6,6]])
print(arr1)

print(arr1[0,:])
print(arr1[1,:])
print(arr1[:,0])
print(arr1[:,:])
print(arr2)