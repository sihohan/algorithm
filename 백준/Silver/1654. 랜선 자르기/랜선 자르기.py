import sys


k, n = map(int, input().split())
assert k <= n, "k <= n"
cables = [int(input()) for _ in range(k)]

l, r = 1, max(cables)
mid = (l + r) // 2
while l <= r:
    n_cable = sum([cable // mid for cable in cables])
    if n_cable < n:
        r = mid - 1
    elif n_cable >= n:
        l = mid + 1

    if l > r:
        break
    mid = (l + r) // 2

print(r)
