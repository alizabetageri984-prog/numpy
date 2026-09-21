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

#example, Q14 is:Create a random vector of size 30 and find the mean value.
random_array = np.random.random(30)
print(random_array.mean())
#Create a 2D array of shape (5, 5) where the border elements are 1 and the inside elements are 0.
import numpy as np

nums = np.ones((5, 5))

nums[1:4, 1:4] = 0

print(nums)
#Q16 🟢Given an existing 2D array, add a border of zeros around it.
nums = np.ones((3, 3))
bordered_nums = np.pad(nums, pad_width=1, mode="constant", constant_values=0)
#np.pad() is a NumPy function used to add extra elements around an array
#mode="constant"Means:Fill the new border with one fixed value.
print(bordered_nums)
#NumPy NaN and Infinity
import numpy as np

print(np.nan)
print(np.inf)
print(-np.inf)
#Q18: Create a 5×5 NumPy matrix where the values below the main diagonal are 1, 2, 3, 4 respectively, and all other values are 0.


nums = np.arange(4, -1, -1)
print(nums)