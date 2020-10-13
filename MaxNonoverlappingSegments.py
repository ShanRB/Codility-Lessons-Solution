def solution(A, B):
    # write your code in Python 3.6
    if not A:
        return 0
    count = 1
    endpoint = B[0]
    for i in range(1,len(A)):
        if A[i] > endpoint:
            count += 1
            endpoint = B[i]
    return count
