from collections import deque


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
prev = [[None] * cols for _ in range(rows)]


dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_bounds(r, c):
    return 0 <= r < rows and 0 <= c < cols

def bfs(start, goal=None):
  
    sr, sc = start
    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = True

    visit_order = []  

    while queue:
        r, c = queue.popleft()
        visit_order.append((r, c))

        if goal and (r, c) == goal:
            break

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if not in_bounds(nr, nc):
                continue
            if visited[nr][nc]:
                continue
            if grid[nr][nc] == 1:  
                continue
            visited[nr][nc] = True
            prev[nr][nc] = (r, c)
            queue.append((nr, nc))

    return visit_order

def reconstruct_path(goal):

    path = []
    cur = goal
    while cur:
        path.append(cur)
        pr, pc = cur
        cur = prev[pr][pc]
    path.reverse()
    return path

order = bfs((0, 0), goal=(5, 5))

for i, (r, c) in enumerate(order, 1):
    print(f"{i}: ({r}, {c})")


    path = reconstruct_path((5, 5))
    print("\n(0,0) -> (5,5) 최단 경로:")

