def star(n):
    print(n * "*")
    if num == n:
        return

    star(n + 1)


num = int(input())
star(1)
