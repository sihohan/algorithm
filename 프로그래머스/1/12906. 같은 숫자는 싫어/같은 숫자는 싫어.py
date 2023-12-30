def solution(arr):
    ans = [arr[0]]
    for n in arr[1:]:
        if ans[-1] != n:
            ans.append(n)
    return ans