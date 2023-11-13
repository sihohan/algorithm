def solution(s):
    nums = list(map(int, s.split(' ')))
    min_, max_ = min(nums), max(nums)
    answer = ' '.join((str(min_), str(max_)))
    return answer