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


nums = np.zeros((5, 5), dtype=int)
nums[1, 0] = 1
nums[2, 0] = 2
nums[2, 1] = 1
nums[3, 0] = 3
nums[3, 1] = 2
nums[3, 2] = 1
nums[4, 0] = 4
nums[4, 1] = 3
nums[4, 2] = 2
nums[4, 3] = 1
print(nums)
#Q19 — Create an 8×8 NumPy matrix with a checkerboard pattern of 0 and 1
checkerboard = np.zeros((8, 8), dtype=int)
checkerboard[::2, 1::2] = 1
checkerboard[1::2, ::2] = 1
print(checkerboard)
#Create a NumPy array with shape (6, 7, 8) and find the index (position) of the 100th element.
array_6x7x8 = np.arange(6 * 7 * 8).reshape(6, 7, 8)
hundredth_index = np.unravel_index(99, array_6x7x8.shape)
print("Index of the 100th element:", hundredth_index)
#reate an 8×8 checkerboard pattern of 0 and 1 using np.tile().
checkerboard_tiled = np.tile([[0, 1], [1, 0]], (4, 4)) #np.tile(pattern, repetitions)
print(checkerboard_tiled)
#Q22:Normalize a 5×5 random NumPy matrix so that its values are between 0 and 1.
random_matrix = np.random.random((5, 5))
normalized_matrix = (random_matrix - random_matrix.min()) / (random_matrix.max() - random_matrix.min())
print(normalized_matrix)

#Q23Create a 5×5 matrix with values 0 and 1 in a checkerboard pattern, then swap the 0s and 1s.
checkerboard_5x5 = np.indices((5, 5)).sum(axis=0) % 2
swapped_checkerboard = 1 - checkerboard_5x5
print(swapped_checkerboard)
#Create a 5×5 matrix with 1s on the border and 0s inside.
nums = np.zeros((5, 5))
bordered_nums = np.pad(nums, pad_width=1, mode="constant", constant_values=1)
print(bordered_nums)

import numpy as np

nums = np.zeros((5, 5), dtype=int)

nums[0, :] = 1
nums[-1, :] = 1
nums[:, 0] = 1
nums[:, -1] = 1

print(nums)

#Q25 — NumPyGiven a 1D array, negate all elements that are between 3 and 8, in place.
nums = np.array([1, 4, 6, 9, 2, 8])
nums[(nums > 3) & (nums <= 8)] *= -1
print(nums)
#Q26 — NumPyCreate a 5×5 matrix with values 0 and 1 in a checkerboard pattern, starting with 1 in the top-left corner
checkerboard_5x5 = 1 - (np.indices((5, 5)).sum(axis=0) % 2)

print(swapped_checkerboard)

#Q27 — NumPy Find the value closest to a given number in a NumPy array.
nums = np.array([1, 5, 10, 15, 20])
target = 12
closest_value = nums[np.abs(nums - target).argmin()]#abs means absolute value — it removes the negative sign.
print("Closest value:", closest_value)#argmin() finds the index of the smallest value.

#Q28 — NumPy Create a 5×5 matrix with random values, then find the minimum and maximum values.
nums = np.random.random((5, 5))
print(nums)
print("Minimum:", nums.min())
print("Maximum:", nums.max())

#Q29 — NumPy Create a 5×5 matrix with 1s on the diagonal and 0s everywhere else.
diagonal_matrix = np.eye(5, dtype=int) #np.eye() creates an identity matrix.
print(diagonal_matrix)
#Q30 — NumPy Create a 5×5 matrix with 0s on the main diagonal and 1s everywhere else.
import numpy as np 
import numpy as np 

diagonal_matrix = np.eye(5, k=1, dtype=int)

print(diagonal_matrix)
#Q31 — NumPy Create a 5×5 matrix with 1s on the main diagonal and 2s on the diagonal above it.
diagonal_matrix = np.eye(5, dtype=int) + np.diag([2] * 4, k=1)
print(diagonal_matrix)
#Q32 — NumPy Create a 5×5 matrix with 1s on the main diagonal and 2s on the diagonal below it
diagonal_matrix = np.eye(5, dtype=int) + np.diag([2] * 4, k=-1)
print(diagonal_matrix)
#Q33 — NumPy Create a 5×5 matrix with 1s on the border and 0s inside.
import numpy as np

nums = np.zeros((5, 5), dtype=int)

nums[0, :] = 1
nums[-1, :] = 1
nums[:, 0] = 1
nums[:, -1] = 1

print(nums)
#Q34 — NumPy Create a 5×5 matrix with 0s on the border and 1s inside
nums = np.ones((3, 3))

bordered_nums = np.pad(
    nums,
    pad_width=1,
    mode="constant",
    constant_values=0
)

print(bordered_nums)
#Q35 — NumPy Create a 5×5 matrix where the values increase from 0 to 24 row by row.
matrix_5x5 = np.arange(25).reshape(5, 5)
print(matrix_5x5)
#next question 
#Q37 — NumPy Create a 5×5 matrix where each row contains the numbers 0, 1, 2, 3, 4
matrix_5x5 = np.tile(np.arange(5), (5, 1))
print(matrix_5x5)
#Q38 — NumPy Create a 5×5 matrix where each column contains the numbers 0, 1, 2, 3, 4
matrix_5x5 = np.tile(np.arange(5).reshape(5, 1), (1, 5))
print(matrix_5x5)
#Q39 — NumPy Create a 5×5 matrix where each element is the sum of its row index and column index
matrix_5x5 = np.indices((5, 5)).sum(axis=0)
print(matrix_5x5)
#Q40 — NumPyCreate a 5×5 matrix where each row contains the numbers 1, 2, 3, 4, 5. 
matrix_5x5 = np.tile(np.arange(1, 6), (5, 1))
print(matrix_5x5)
