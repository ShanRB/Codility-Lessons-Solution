def solution(N, P, Q):
    # write your code in Python 3.6
    factors = [0] * (N+1)
    i = 2
    while (i*i <= N):
        if (factors[i] == 0):
            k = i*i
            while (k <= N):
                factors[k] = i
                k += i
        i += 1
    semiprime = []
    for i in range(N+1):
        if factors[i] == 0:
            semiprime.append(0)
        else:
            if factors[i//factors[i]] == 0:
                semiprime.append(1)
            else:
                semiprime.append(0)
    for i in range(1,N+1):
        semiprime[i] += semiprime[i-1]

    result = []
    for j in range(len(P)):
        result.append(semiprime[Q[j]]-semiprime[P[j]-1])
    return result