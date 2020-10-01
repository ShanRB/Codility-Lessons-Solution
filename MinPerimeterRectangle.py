def solution(N):
    # write your code in Python 3.6
    i = 2
    perimeter = (N+1) * 2
    while i*i <= N:
        if N % i == 0:
            perimeter = min(perimeter, 2*(i+N//i))
        i += 1
    return perimeter