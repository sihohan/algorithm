def solution(n):
    cnt = 1
    for i in range(1, n + 1):
        sum_ = 0
        for j in range(i, n + 1):
            sum_ += j
            if sum_ > n:
                break
                
        if sum_ - j == n:
            cnt += 1
        
    return cnt