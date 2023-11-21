def solution(n):
    return sum([d for d in range(1, n + 1) if n % d == 0])