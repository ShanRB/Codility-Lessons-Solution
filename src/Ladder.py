def fib(n):
    fib = [0,1]
    for _ in range(n):
        fib.append(fib[-1] + fib[-2])
    return fib[1:]
    
def solution(A, B):
    # write your code in Python 3.6
    n = max(A)
    fibs = fib(n)
    result = []
    for i in range(len(A)):
        result.append(fibs[A[i]] & ((1 << B[i]) - 1))
    return result
