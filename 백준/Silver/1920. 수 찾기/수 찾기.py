import bisect

input()
a = sorted(list(map(int, input().split())))
input()
m = list(map(int, input().split()))

for x in m:
    if bisect.bisect_right(a, x) - bisect.bisect_left(a, x) > 0:
        print(1)
    else:
        print(0)
