def solution(A):
    # write your code in Python 3.6
    sums = [A[0]]
    for i in range(1,len(A)):
        maxV = float("-inf")
        for j in range(max(0,i-6),i):
            maxV = max(maxV,A[i]+sums[j])
        sums.append(maxV)
    return sums[-1]