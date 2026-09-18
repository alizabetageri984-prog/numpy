#dataset normalization mini project
import numpy as np
arr = np.array([50, 100, 150, 200, 250])
normalized_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
print(normalized_arr)

arr_age = np.array([25, 30, 40, 35, 50])
normalized_arr_age = (arr_age - np.min(arr_age)) / (np.max(arr_age) - np.min(arr_age))
print(normalized_arr_age)

arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
normalized_arr_2d = (arr_2d - np.min(arr_2d)) / (np.max(arr_2d) - np.min(arr_2d))
print(normalized_arr_2d)

arr_2d = np.array([
    [25, 40000],
    [40, 90000],
    [30, 60000]
])

col_min = np.min(arr_2d, axis=0)
col_max = np.max(arr_2d, axis=0)

normalized_arr_2d = (arr_2d - col_min) / (col_max - col_min)
print(normalized_arr_2d) 

#z score 
heights = np.array([140, 145, 150, 155, 200])
z_score = (heights - np.mean(heights)) /np.std(heights)
print(z_score)

arr_2d = np.array([
    [25, 40000],
    [40, 90000],
    [30, 60000]
])
col_mean = np.mean(arr_2d, axis=0)
col_std = np.std(arr_2d, axis=0)
z_score = (arr_2d - col_mean) / col_std
print(z_score)
arr_2d = np.array([
    [25, 40000],
    [40, 90000],
    [30, 60000]
])

row_mean = np.mean(arr_2d, axis=1)
print(row_mean)