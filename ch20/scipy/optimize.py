from scipy.optimize import minimize

def f(x):
    return x**2 +4*x +4

result = minimize(f, x0=0)
print(f"Optimal value:{result.x}")