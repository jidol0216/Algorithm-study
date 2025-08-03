
grid = [
    [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0]
]

rows = len(grid)
cols = len(grid[0])


visited = [[False] * cols for _ in range(rows)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_bounds(r, c):
    return 0 <= r < rows and 0 <= c < cols

def dfs(r, c, visit_order):
  
    if not in_bounds(r, c) or grid[r][c] == 1 or visited[r][c]:
        return
    visited[r][c] = True
    visit_order.append((r, c)) 

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        dfs(nr, nc, visit_order)


order = []
dfs(0, 0, order)


for idx, (r, c) in enumerate(order):
    print(f"{idx+1}: ({r}, {c})")
