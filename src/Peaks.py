import math
def checkBlock(blockSize,peaks,N):
    i = 0
    pos = peaks[0]
    while pos != 0:
        if pos > i + blockSize:
            break;
        if pos >= i and pos < i + blockSize:
            i += blockSize
        pos = peaks[pos+1]
    if i == N:
        return True
    return False
def solution(A):
    # write your code in Python 3.6
    N = len(A)
    if N < 3:
        return 0
    peaks = [0 for _ in range(N)]
    peakCount = 0
    for i in range(N-2,0,-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peaks[i] = i
            peakCount += 1
        else:
            peaks[i] = peaks[i+1]
    peaks[0] = peaks[1]
    if not peakCount:
        return 0

    for n in range(peakCount,0,-1):
        if N % n == 0:
            divisor = N // n
            if checkBlock(divisor,peaks,N):
                return n 
    return 0  

if __name__ == '__main__':
    A = [1,2,3,4,3,4,1,2,3,4,6,2]
    print(f'results: {solution(A)}')