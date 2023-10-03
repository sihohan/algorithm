import bisect

input()
a = sorted(list(map(int, input().split())))
input()
m = list(map(int, input().split()))

for x in m:
    idx = bisect.bisect_left(a, x)
    if (idx != len(a)) and (a[idx] == x):
        print(1)
    else:
        print(0)
