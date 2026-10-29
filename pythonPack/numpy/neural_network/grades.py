import numpy as np

grades = np.array([
    [85, 90, 78],
    [70, 75, 80],
    [95, 88, 92],
    [60, 65, 70],
    [88, 92, 95]
])
print(grades)
shapes = np.shape(grades)
matrix_size = shapes[0]*[1]
grades_st_three = grades[2]


numpy_score = grades[4, 2]
print(numpy_score)
average_scores = np.mean(grades, axis=1)
print(average_scores)
