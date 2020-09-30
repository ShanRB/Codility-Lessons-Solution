def solution(H):
    # write your code in Python 3.6
    stack = []
    total = 0
    for n in H:
        if not stack:
            stack.append(n)
        if n == stack[-1]:
            continue;
        if n > stack[-1]:
            stack.append(n)
        if n < stack[-1]:
            while(stack):
                l = stack.pop()
                if l > n:
                    total += 1
                if l < n:
                    stack.append(l)
                    break;
            stack.append(n)
    return total + len(stack)