def solution(A):
    # write your code in Python 3.6
    maxEnd = A[0]
    maxSlice = maxEnd
    for i in range(1,len(A)):
        maxEnd = max(A[i], maxEnd+A[i])
        maxSlice = max(maxEnd,maxSlice)
    return maxSlice