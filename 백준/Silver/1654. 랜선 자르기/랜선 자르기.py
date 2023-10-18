import sys

k, n = map(int, input().split())
assert k <= n, "k <= n"
cables = [int(input()) for _ in range(k)]

if n == 1:
    print(cables[0])  # instead of max(cables) since k is also 1 due to assertion
    sys.exit()

l, r = 1, max(cables)
mid = (l + r) // 2
while l <= r:
    n_cable = sum([cable // mid for cable in cables])
    if n_cable < n:
        r = mid - 1
    elif n_cable >= n:
        l = mid + 1

    mid = (l + r) // 2

print(mid)
