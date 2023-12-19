def solution(arr1, arr2):
    res = []
    for i, (row1, row2) in enumerate(zip(arr1, arr2)):
        res.append([])
        for n1, n2 in zip(row1, row2):
            res[i].append(n1 + n2)
    return res