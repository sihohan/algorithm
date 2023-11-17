import math


def solution(n):
    sq_rt = math.sqrt(n)
    return (int(sq_rt) + 1) ** 2 if math.floor(sq_rt) ** 2 == n else -1