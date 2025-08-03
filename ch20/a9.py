from scipy.optimize import root


def func(x):
    return (x - 3)**2


i = 0

solution = root(func, i)

print( solution.x)
