while True:
    phrase = input()
    if phrase == '#':
        break
    
    cnt = 0
    for char in phrase.lower():
        if char in ('a', 'e', 'i', 'o', 'u'):
            cnt += 1
    
    print(cnt)