def solution(A):
    # write your code in Python 3.6
    if len(A) < 3:
        return 0
    A.sort()
    count = 0
    for i in range(0,len(A)-2):
        j = i + 1
        k = j + 1
        while(k < len(A)):
            if A[i]+A[j] > A[k]:
                count += k - j
                k += 1
            elif j < k - 1:
                j += 1
            else:
                j += 1
                k += 1
    return count