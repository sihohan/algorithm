digits = list(map(int, input().split()))
print(sum(list(map(lambda digit: digit ** 2, digits))) % 10)