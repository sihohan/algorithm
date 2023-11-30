def solution(num):
    if num == 1:
        return 0
    
    cnt = 0
    while num > 1:
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
        
        cnt += 1
    
    return cnt if cnt < 500 else -1