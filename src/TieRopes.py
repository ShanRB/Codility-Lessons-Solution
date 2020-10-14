def solution(K, A):
    # write your code in Python 3.6
    count = 0
    currLen = 0
    for i in range(len(A)):
        currLen += A[i]
        if currLen >= K:
            count += 1
            currLen = 0
    return count