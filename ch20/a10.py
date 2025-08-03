import numpy as np


group_A = [80, 85, 90, 75, 95]


mean = np.mean(group_A)
median = np.median(group_A)
variance = np.var(group_A, ddof=1)  
std_dev = np.std(group_A, ddof=1)   
min_val = np.min(group_A)
max_val = np.max(group_A)

print(f"평균: {mean}")
print(f"중앙값: {median}")
print(f"분산: {variance}")
print(f"표준편차: {std_dev}")
print(f"최소값: {min_val}")
print(f"최대값: {max_val}")
