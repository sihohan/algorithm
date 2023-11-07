import sys

input = sys.stdin.readline


def star(n):
    if n == 0:
        return

    print("* " * int((num / 2).__ceil__()))
    if num > 1:
        print(" *" * (num // 2))

    star(n - 1)


num = int(input())
star(num)
