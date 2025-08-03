import statsmodels.api as sm
import numpy as np


x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

x_with_const = sm.add_constant(x)


model = sm.OLS(y, x_with_const)
results = model.fit()


print("절편 (intercept):", results.params[0])
print("기울기 (slope):", results.params[1])
