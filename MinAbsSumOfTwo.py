def solution(A):
    # write your code in Python 3.6
    A.sort()
    currMin = abs(A[0])*2
    i = 0
    j = len(A) - 1
    while(i <= j):
        currMin = min(currMin, abs(A[i]+A[j]))
        if abs(A[i]) >= abs(A[j]):
            i += 1
        else:
            j -= 1
    return currMin