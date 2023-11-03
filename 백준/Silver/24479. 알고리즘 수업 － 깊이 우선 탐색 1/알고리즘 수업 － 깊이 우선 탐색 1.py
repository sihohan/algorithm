import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(adj, r, visited, vertex_to_order):
    global order
    visited[r] = True
    order += 1
    vertex_to_order[r] = order
    for j in sorted(adj[r]):
        if not visited[j]:
            dfs(adj, j, visited, vertex_to_order)


n, m, r = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    adj[i].append(j)
    adj[j].append(i)

visited = [False] * (len(adj))
vertex_to_order = {vertex: 0 for vertex in range(1, n + 1)}
order = 0
dfs(adj, r, visited, vertex_to_order)
for _, v in sorted(vertex_to_order.items()):
    print(v)
