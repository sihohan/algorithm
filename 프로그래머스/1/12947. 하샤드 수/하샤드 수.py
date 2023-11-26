def solution(x):
    return True if x % sum([int(n) for n in str(x)]) == 0 else False