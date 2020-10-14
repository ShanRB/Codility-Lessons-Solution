def solution(A):
    # write your code in Python 3.6
    if not A:
        return 0
    diff = []
    for i in range(1,len(A)):
        diff.append(A[i]-A[i-1])
    maxEnd = max(0,diff[0])
    maxSlice = maxEnd
    for i in range(1,len(diff)):
        maxEnd = max(maxEnd+diff[i],0)
        maxSlice = max(maxSlice,maxEnd)
    return maxSlice