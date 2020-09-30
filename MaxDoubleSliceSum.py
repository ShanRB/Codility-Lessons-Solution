def solution(A):
    # write your code in Python 3.6
    endMax = [0]
    for i in range(1,len(A)):
        endMax.append(max(endMax[-1]+A[i], 0))
    startMax = [0 for _ in range(len(A))]
    for i in range(len(A)-2,-1,-1):
        startMax[i] = max(startMax[i+1]+A[i], 0)
    maxSlice = 0
    for i in range(1,len(A)-1):
        maxSlice = max(maxSlice, endMax[i-1]+startMax[i+1])
    return maxSlice