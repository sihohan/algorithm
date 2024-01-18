n, m = map(int, input().split())
diff = n - m
print(diff if diff > 0 else -diff)