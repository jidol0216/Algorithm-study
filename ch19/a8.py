import numpy as np


arr = np.arange(1, 11)

squared = arr ** 2

mean_val = squared.mean()
max_val = squared.max()
min_val = squared.min()


print("원본 배열:", arr)
print("제곱 배열:", squared)
print(f"평균: {mean_val}, 최댓값: {max_val}, 최솟값: {min_val}")
