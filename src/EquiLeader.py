def solution(A):
    # write your code in Python 3.6
    count = 0
    value = None
    for n in A:
        if count == 0:
            value = n
            count += 1
        else:
            if n == value:
                count += 1
            else:
                count -= 1
                if count == 0:
                    value = n
                    count += 1
    if count == 0:
        return 0
    count = 0
    left = [0 for _ in range(len(A))]
    for i in range(len(A)):
        if A[i] == value:
            count += 1
            if i == 0:
                left[i] = 1
            else:
                left[i] = left[i-1] + 1
        else:
            if i == 0:
                left[i] = 0
            else:
                left[i] = left[i-1]
    if count <= len(A)/2:
        return 0
    count = 0
    for i in range(len(left)):
        if left[i] > (i+1)/2 and left[-1]-left[i] > (len(left)-i-1)/2:
            count += 1
    return count