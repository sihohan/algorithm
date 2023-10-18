# https://www.acmicpc.net/problem/1654
import sys

k, n = map(int, input().split())
assert k <= n, "k <= n"
cables = [int(input()) for _ in range(k)]

# length = 1
# n_cable = 1e6 + 1
# while n_cable >= n:
#     n_cable = sum([cable // length for cable in cables])
#     length += 1

# while 1:
#     n_cable = sum([cable // length for cable in cables])
#     if n_cable < n:
#         break
#     length += 1

# print(length - 2)

# nums = [1, 2, 6, 10, 200, 205]

# def binary_search(nums, to_find):
#     l, r = 0, len(nums) - 1
#     mid = (l + r) // 2
#     while l <= r:
#         if to_find == nums[mid]:
#             return True

#         if to_find < nums[mid]:
#             r = mid - 1
#         elif to_find > nums[mid]:
#             l = mid + 1

#         mid = (l + r) // 2

#     return False


if n == 1:
    print(max(cables))
    sys.exit()
# if max(cables) < n:
#     print(1)
#     sys.exit()

l, r = 1, max(cables)
# length2n_cable = {
#     length: sum([cable // length for cable in cables]) for length in range(l, r + 1)
# }
# print(length2n_cable)
mid = (l + r) // 2
# print()
# print(l, mid, r)
while l <= r:
    # n_cable = length2n_cable.get(mid)
    n_cable = sum([cable // mid for cable in cables])
    if n_cable < n:
        r = mid - 1
    elif n_cable >= n:
        l = mid + 1

    if l > r:
        # if n_cable < n:
        #     mid -= 1
        break
    mid = (l + r) // 2
#     print(l, mid, r)

# print()
# print(mid)
print(r)
