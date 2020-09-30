def solution(A):
    left = A[0]
    right = sum(A[1:])
    diff = abs(right - left)
    for i in range(1,len(A)-1):
        left += A[i]
        right -= A[i]
        diff = min(diff,abs(left-right))
    return diff