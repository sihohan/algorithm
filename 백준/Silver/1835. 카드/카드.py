from collections import deque

n = int(input())
dq = deque()

for i in reversed(range(1, n + 1)):
    dq.appendleft(i)
    if i == n:
        continue

    for _ in range(i):
        dq.appendleft(dq.pop())

print(*dq)
