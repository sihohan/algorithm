from queue import Queue


def dfs(adj, n, v):
    visited = [False] * (n + 1)  # Start from node 0 for clear indexing
    route = []
    search_from = [v]
    while search_from:
        i = search_from.pop()
        if visited[i]:
            continue

        visited[i] = True
        route.append(i)
        for j in sorted(adj[i], reverse=True):
            if not visited[j]:
                search_from.append(j)

    return route


def bfs(adj, n, v):
    visited = [False] * (n + 1)
    visited[v] = True
    route = []
    search_from = Queue()
    search_from.put(v)
    while search_from.qsize() > 0:
        i = search_from.get()
        route.append(i)
        for j in sorted(adj[i]):
            if not visited[j]:
                visited[j] = True
                search_from.put(j)

    return route


n, m, v = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    adj[i].append(j)
    adj[j].append(i)

print(*dfs(adj, n, v))
print(*bfs(adj, n, v))
