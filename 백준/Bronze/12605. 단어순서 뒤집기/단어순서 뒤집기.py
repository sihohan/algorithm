n = int(input())
for i in range(n):
    words = input().split()
    reverse = []
    while words:
        reverse.append(words.pop())
    print(f'Case #{i + 1}: {" ".join(reverse)}')
