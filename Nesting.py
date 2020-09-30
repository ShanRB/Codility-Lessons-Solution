def solution(S):
    # write your code in Python 3.6
    if not S:
        return 1
    stack = []
    for s in S:
        if s == '(':
            stack.append(s)
        else:
            if not stack:
                return 0
            else:
                stack.pop()
    if stack:
        return 0
    return 1
