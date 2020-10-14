def solution(S):
    # write your code in Python 3.6
    openbracket = '([{'
    closebracket = ')]}'
    pairs = {')':'(', ']':'[', '}':'{'}
    if not S:
        return 1
    stack = []
    for s in S:
        if s in openbracket:
            stack.append(s)
        if s in closebracket:
            if not stack:
                return 0
            if pairs[s] != stack.pop():
                return 0
    if stack:
        return 0
    return 1
