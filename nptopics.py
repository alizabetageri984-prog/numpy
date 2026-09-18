import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a)#prints whole array
print(a.dtype) #gives the amount of data used 
print(a.shape)# gives size of array in tuple
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.dtype)
print(b.shape)
print(b.size)
print(b.ndim)

#array reshaping 
arr = np.arange(12)
print("original array:" , arr)
reshaped_arr = arr.reshape(3, 4)
print("reshaped array:" , reshaped_arr)
print("\n flattened array:" , reshaped_arr.flatten())
#raveling the array 
#returns a view of the original array whenever possible instead of a copy.
raveled_arr = reshaped_arr.ravel()
print("raveled array:" , raveled_arr)
#transposing the array 
transposed_arr = reshaped_arr.T
print("transposed array:" , transposed_arr)
#indexing and slicing
print("element at index (1, 2):" , reshaped_arr[1, 2])
arr = np.array([10, 20,30, 40, 50])
print("element at index 1 to 3:" , arr[1:4])
print(arr[0])
print(arr[-1])
grid = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("element at index (1, 2):" , grid[1, 2])
print("element at index (0, 2):" , grid[0, 2])
print("row at index 1:" , grid[1, :])
print("column at index 2:" , grid[:, 2])
print("entire row" , grid[1])
print("entire column" , grid[:, 2])
##sorting the array
unsorted_arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5])
sorted_arr = np.sort(unsorted_arr)
print(sorted_arr)
#2D array sorting
unsorted_arr_2d = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
sorted_arr_2d = np.sort(unsorted_arr_2d , axis = 0)#sorting the array along the first axis(columns)
print(sorted_arr_2d)
sorted_arr_2d = np.sort(unsorted_arr_2d , axis = 1)#sorting the array along the second axis(rows)
print(sorted_arr_2d)

#filtering the array
numbers = np. array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even_numbers = numbers[numbers % 2 == 0]
print(even_numbers)

#filtering  2D array 
filter_2d = unsorted_arr_2d[unsorted_arr_2d > 3]
print(filter_2d)

#masking the array 
mask = numbers > 5
masked_numbers = numbers[mask]
print(masked_numbers)
## add or removing data 
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
#adding data 
combined_arr = np.concatenate((arr1, arr2))
print(combined_arr)
#remoivng data
arr = np.array([1, 2, 3, 4, 5])
arr = np.delete(arr, 2) #removes the element at index 2 
print(arr)
#array compatability
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9, 10])
print("compatibility of arr1 and arr2:" , arr1.shape == arr2.shape)
print("compatibility of arr1 and arr3:" , arr1.shape == arr3.shape)
#adding row 
original = np.array([[1, 2], [3, 4]])
new_row = np.array([[5, 6]])
combined_rows = np.vstack((original, new_row))
print(original)
print(combined_rows)
#adding column
original = np.array([[1, 2], [3, 4]])
new_column = np.array([[5], [6]])
combined_columns = np.hstack((original, new_column))
print(original)
print(combined_columns)
#boardcasting
import numpy as np
a = np.array([[1, 2, 3, 4], [ 5, 6, 7, 8]])
b = np.array([100, 200, 300, 400])
print(a + b)
print((a + b).shape)
#vectorization
arr = np.array([1, 2, 3, 4, 5])
print(arr * 3)
print(arr - 1)
print(arr ** 2)
arr = np.array([1, 4, 9, 16])
print(np.sqrt(arr))
print(np.exp(arr))     # e raised to the power of each element
#aggergation  functions 
arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
#for 2D array
arr_2d = np.array([
    [80, 90, 100, 88],
    [70, 85, 95, 92],
    [75, 80, 85, 90]
])
print(np.sum(arr_2d))
print(np.mean(arr_2d))
print(np.max(arr_2d))
print(np.min(arr_2d))
print(np.mean(arr_2d, axis=1))#mean performing operation along the rows horixantally 
print(np.mean(arr_2d, axis = 0))#mean performing operation along the columns vertically 
#multiplication of arrays #@multiplication operator is used for matrix multiplication the corresponding element pairs and add them together to produced a single value 
quantities = np.array([
    [2, 3, 1],   # customer 1
    [1, 0, 4]    # customer 2
])
prices = np.array([10, 5, 20])

totals = quantities @ prices
print(totals)

#matrix multiplication 
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = a @ b
print(result)
np.random.rand(3)        # 3 random floats between 0 and 1
np.random.randint(1, 10, size=5)   # 5 random integers between 1 and 10 (10 excluded)
np.random.randn(3)       # 3 random numbers from a "normal distribution" (bell curve, centered at 0)
print(np.random.rand(3))
print(np.random.randint(1, 10, size=5))
print(np.random.randn(3))
np.random.seed(42)
print(np.random.rand(3))
np.random.seed(42)
print(np.random.rand(3))