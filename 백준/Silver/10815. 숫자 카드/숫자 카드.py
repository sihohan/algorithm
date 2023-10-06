input()
search_from = list(map(int, input().split()))
input()
to_find = list(map(int, input().split()))

dict_ = {}
for x in search_from:
    dict_.setdefault(x, 0)
    dict_[x] += 1

ans = []
for y in to_find:
    cnt = dict_.get(y)
    ans.append(cnt if cnt is not None else 0)

print(*ans)
