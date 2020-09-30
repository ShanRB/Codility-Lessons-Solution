def solution(N, A):
    # write your code in Python 3.6
    result = [0 for i in range(N)]
    currMax = 0
    lastMax = 0
    for n in A:
        if n <= N:
            result[n-1] = max(lastMax,result[n-1]) + 1
            currMax = max(currMax,result[n-1])
        else:
            lastMax = currMax
    for i in range(N):
        result[i] = max(result[i],lastMax)
    return result

if __name__ == '__main__':
    A = [3,4,4,6,1,4,4]
    N = 5
    print(solution(N,A))