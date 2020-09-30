def solution(A):
    # write your code in Python 3.6
    nums = set(A)
    n = len(A)
    if len(nums) != n:
        return 0
    if max(A) != n:
        return 0
    total = n*(n+1) // 2
    if sum(A) == total:
        return 1
    return 0