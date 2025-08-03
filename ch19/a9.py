import numpy as np


np.random.seed(0) 
matrix = np.random.randint(1, 13, size=(3, 4))

print("원본 행렬:")
print(matrix)


max_per_row = matrix.max(axis=1)

print("각 행의 최댓값:", max_per_row)
