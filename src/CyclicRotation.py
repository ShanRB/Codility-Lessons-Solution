def solution(A, K):
    # write your code in Python 3.6
    if not A:
        return A
    size = len(A)
    while (K >= size):
        K -= size
    # find break index
    newHead = size - K
    return A[newHead:]+A[:newHead]