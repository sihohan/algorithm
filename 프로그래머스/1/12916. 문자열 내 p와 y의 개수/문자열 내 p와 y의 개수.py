def solution(s):
    cnt_p, cnt_y = 0, 0
    for char in s:
        if char.lower() == 'p':
            cnt_p += 1
        elif char.lower() == 'y':
            cnt_y += 1
    
    if (cnt_p == cnt_y):
        return True
    else:
        return False