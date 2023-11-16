def solution(n):
    answer = None
    for x in range(1, n):
        if n % x == 1:
            answer = x
            break
            
    return answer