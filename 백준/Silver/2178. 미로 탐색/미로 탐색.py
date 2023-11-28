import sys
from queue import Queue

input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())
maze = [[int(digit) for digit in input().strip()] for _ in range(n)]
adj = {}
visited = {}
prev = {}
for r in range(n):
    row = maze[r]
    adj[r] = {}
    visited[r] = {}
    prev[r] = {}

    for c in range(m):
        adj[r][c] = []
        visited[r][c] = True if ((r == 0) and (c == 0)) else False

        for i in range(4):
            r_dr, c_dc = r + dr[i], c + dc[i]
            if (r_dr < 0) or (c_dc < 0) or (n - 1 < r_dr) or (m - 1 < c_dc):  # Off-grid
                continue

            node = maze[r_dr][c_dc]
            if node == 1:
                adj[r][c].append((r_dr, c_dc))


search_from = Queue()
search_from.put((0, 0))
while search_from.qsize() > 0:
    x, y = search_from.get()
    if (x == n - 1) and (y == m - 1):  # Target node reached
        break

    for x_adj, y_adj in adj[x][y]:
        if not visited[x_adj][y_adj]:
            visited[x_adj][y_adj] = True
            search_from.put((x_adj, y_adj))
            prev[x_adj][y_adj] = (x, y)

shortest_path = [(n - 1, m - 1)]
while (x, y) != (0, 0):
    x, y = prev[x][y]
    shortest_path.insert(0, (x, y))

print(len(shortest_path))
