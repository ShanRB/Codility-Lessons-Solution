def solution(A, B):
    # write your code in Python 3.6
    n = len(A)
    alive = 0
    stack = []
    for i in range(n):
        if B[i]:
           stack.append(i)
        else:
            if not stack:
                alive += 1
            else:
                while(True):
                    downfish = stack.pop()
                    if A[downfish] > A[i]:
                        stack.append(downfish)
                        break;
                    else:
                        if not stack:
                            alive += 1
                            break;
    alive += len(stack)
    return alive