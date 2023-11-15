def solution(absolutes, signs):
    answer = sum([n if sign else -n for n, sign in zip(absolutes, signs)])
    return answer