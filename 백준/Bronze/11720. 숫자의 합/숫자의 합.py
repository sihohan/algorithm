import sys

input = sys.stdin.readline

n = int(input())
digits = input()
print(sum([int(digit) for digit in digits.strip()]))
