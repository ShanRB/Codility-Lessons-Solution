def solution(A, B, K):
    # write your code in Python 3.6
    while (A % K != 0):
        A += 1
    while (B % K != 0):
        B -= 1
    return (B-A)//K + 1