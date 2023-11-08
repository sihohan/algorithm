import sys

input = sys.stdin.readline


def recursion(s, l, r):
    global cnt_recur
    cnt_recur += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)


def is_palindrome(s):
    return recursion(s, 0, len(s) - 1)


t = int(input())
for _ in range(t):
    cnt_recur = 0
    s = input().strip()
    print(is_palindrome(s), cnt_recur)
