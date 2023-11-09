import sys

input = sys.stdin.readline

nums = []
for _ in range(5):
    num = int(input())
    nums.append(num)

print(int(sum(nums) / len(nums)))
print(sorted(nums)[2])
