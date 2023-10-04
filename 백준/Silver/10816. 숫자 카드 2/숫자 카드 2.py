import bisect

input()
serach_from = sorted(list(map(int, input().split())))
input()
to_find = list(map(int, input().split()))

ans = []
for x in to_find:
    ans.append(bisect.bisect_right(serach_from, x) - bisect.bisect_left(serach_from, x))

print(*ans)
