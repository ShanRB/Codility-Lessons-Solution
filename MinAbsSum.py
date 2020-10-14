def solution(A):
    # write your code in Python 3.6
    if not A:
        return 0
    if len(A) == 1:
        return abs(A[0])
    S = 0
    count = {}
    for i in range(len(A)):
        A[i] = abs(A[i])
        S += A[i]
        if A[i] in count:
            count[A[i]] += 1
        else:
            count[A[i]] = 1
    dp = [-1 for _ in range(S+1)]
    dp[0] = 0
    for k,v in count.items():
        for i in range(S+1):
            if dp[i] >= 0:
                dp[i] = v
            else:
                if i >= k and dp[i-k] > 0:
                    dp[i] = dp[i-k]-1

    for x in range(S//2,-1,-1):
        if dp[x] >= 0:
            return  S - 2*x
    return -1
