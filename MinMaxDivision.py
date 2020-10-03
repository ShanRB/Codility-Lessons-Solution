def maxBlockCount(A,maxValue):
    count = 1
    accSum = 0
    for n in A:
        accSum += n
        if accSum > maxValue:
            accSum = n
            count += 1
    return count

def solution(K, M, A):
    # write your code in Python 3.6
    if K == 1:
        return sum(A)
    if len(A) <= 1:
        return sum(A)
    left = max(A)
    right = sum(A)
    
    while (left < right):
        mid = left + (right-left)//2
        if maxBlockCount(A,mid) > K:
            left = mid + 1
        else:
            right = mid
    return right