import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])


x_with_const = sm.add_constant(x)


model = sm.OLS(y, x_with_const)
results = model.fit()

y_pred = results.predict(x_with_const)


plt.scatter(x, y, color='blue', label='Data points')      
plt.plot(x, y_pred, color='red', label='Regression line') 

plt.title('Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
