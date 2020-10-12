def solution(A):
    # write your code in Python 3.6
    count = 1
    front = 0
    back = len(A) - 1
    currValue = max(abs(A[0]),abs(A[-1]))
    while (front <= back):
        frontV = abs(A[front])
        if frontV == currValue:
            front += 1
            continue
        backV = abs(A[back])
        if backV == currValue:
            back -= 1
            continue
        if frontV >= backV:
            front += 1
            currValue = frontV
        elif frontV < backV:
            back -= 1
            currValue = backV
        count += 1
    return count