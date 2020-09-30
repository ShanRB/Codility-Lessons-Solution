def solution(A):
    # write your code in Python 3.6
    sums = [0 for i in range(len(A)+1)]
    for i in range(len(A)-1,-1,-1):
        sums[i] = sums[i+1] + A[i]
    total = 0
    for i in range(len(A)):
        if A[i] == 0:
            total += sums[i]
        if total > 10**9:
            return -1
    return total