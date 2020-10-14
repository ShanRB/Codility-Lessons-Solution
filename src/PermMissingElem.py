def solution(A):
    # write your code in Python 3.6
    n = len(A)
    return (n+2)*(n+1)//2 - sum(A)
