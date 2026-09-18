import numpy as np

null_vector = np.zeros(10)
print(null_vector)
#Question 4: How to find the memory size of any array?
arr = np.array([ 1, 2, 4, 6])
print(arr.size)#4 elements
print(arr.itemsize)#(each element takes 8 bytes, since your numbers are stored as int64 by default).
total_memory = arr.size * arr.itemsize
print(total_memory)
#Question 6: Create a null vector of size 10, but the fifth value should be 1
null_vector = np.zeros(10)
null_vector[4] = 1
print(null_vector)
#Question 7: Create a vector with values ranging from 10 to 49.
vector = np.arange(10, 50)
print(vector)
#Reverse a vector (first element becomes last).
a = np.array([10, 20, 30, 40, 50])
print(a[::-1])
# Output: [50 40 30 20 10]
#Create a 3x3 matrix with values ranging from 0 to 8.
arr = np.arange(9)
print(arr)
arr_3x3 = arr.reshape(3, 3)
print(arr_3x3)
#Question 10: Find indices of non-zero elements from [1, 2, 0, 0, 4, 0]
nums = np.array([1, 2, 0, 0, 4, 0 ])
result = np.nonzero(nums)
print(result)
print(result[0])
#: Create a 3x3 identity matrix
identity = np.eye(3)
print(identity)
#Create a 3x3x3 array with random values.
random_array = np.random.random((3, 3, 3))# 3D: 3 sheets, each 3 rows x 3 columns
print(random_array)
#Question 13: create a 10x10 array with random values and find the minimum and maximum values?
random_10x10 = np.random.random((10, 10))
print(random_10x10)
print("Minimum:", random_10x10.min())
print("Maximum:", random_10x10.max())
