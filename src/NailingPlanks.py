def solution(A, B, C):
    # write your code in Python 3.6
    maxIndex = max(max(A),max(B),max(C))+1
    result = -1
    left = 0
    right = len(C)
    while left <= right:
        mid = left + (right-left)//2
        
        nails = [0 for _ in range(maxIndex)]
        for i in range(mid):
            nails[C[i]] = 1
        for i in range(1,maxIndex):
            nails[i] += nails[i-1]
        isAllCover = True
        for i in range(len(A)):
            if (nails[B[i]] - nails[A[i]-1] == 0):
                isAllCover = False
                break;
        if isAllCover:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

if __name__ == '__main__':
    A = [2]
    B = [2]
    C = [1]
    print(solution(A,B,C))