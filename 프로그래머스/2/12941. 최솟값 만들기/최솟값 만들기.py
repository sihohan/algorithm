def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    while A:
        min_ = A.pop(0)
        max_ = B.pop(-1)
        answer += (min_ * max_)
        
    return answer