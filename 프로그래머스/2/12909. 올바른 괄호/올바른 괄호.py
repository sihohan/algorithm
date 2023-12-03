def solution(s):
    # Early return conditions
    if len(s) % 2 != 0:
        return False
    if s[0] == ')' or s[-1] == '(':
        return False
    
    check = s[0]
    for parenthesis in s[1:]:
        check += parenthesis
        if check[-2:] == '()':
            check = check[:-2]
    
    return True if not check else False