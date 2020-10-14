def solution(N):
    # write your code in Python 3.6
    while (N % 2 == 0):
        N = N // 2
    currMax = 0
    count = 0
    while (N > 1):
        if N % 2 == 1:
            currMax = max(count, currMax)
            count = 0
        else:
            count += 1
        N = N // 2
    currMax = max(count, currMax)
    return currMax
