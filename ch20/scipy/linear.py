from scipy.linalg import solve
A= [[3,1],[1,2]]

b = [9,8]

x = solve(A,b)
print(f"Solution:{x}")