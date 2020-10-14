def fibonacci(n):
    f0 = 0
    f1 = 1
    fib = []
    f = f0 + f1
    while f <= n:
        fib.append(f)
        f0, f1 = f1, f
        f= f0 + f1
    return fib
    
def solution(A):
    # write your code in Python 3.6
    if not A:
        return 1
    fib = fibonacci(len(A)+1)
    A.append(1)
    jumps = [-1] * len(A)
    for f in fib:
        if A[f-1]:
            jumps[f-1] = 1

    for i in range(len(A)):
        if (A[i] == 1 and jumps[i] < 0):
            paths = [jumps[i-f]+1 for f in fib if i-f >= 0 and jumps[i-f]>0]
            if paths:
                jumps[i] = min(paths)
    return jumps[-1]
