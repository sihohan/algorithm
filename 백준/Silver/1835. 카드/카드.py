from collections import deque

n = int(input())
dq = deque()

# dq.append(3)
# print(dq)
# dq.append(4)
# print(dq)
# dq.appendleft(2)
# print(dq)  # deque([2, 3, 4])

for i in reversed(range(1, n + 1)):
    dq.appendleft(i)
    if i == n:
        continue

    for _ in range(i):  # 0, 1, 2
        dq.appendleft(dq.pop())

print(*dq)
