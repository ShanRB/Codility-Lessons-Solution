def solution(M, A):
    # write your code in Python 3.6
    seen = [0] * (M + 1)
    count = 0
    i,j = 0,0
    while(i < len(A) and j < len(A)):
        if seen[A[j]]:
            seen[A[i]] = 0
            i += 1
        else:
            seen[A[j]] = 1
            count += j - i + 1
            j += 1
        if count > 1e9:
            return int(1e9)
    return count