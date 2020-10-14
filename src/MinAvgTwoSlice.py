def solution(A):
    # write your code in Python 3.6
    minAvg = float("inf")
    minP = 0
    
    for i in range(len(A)-1):
        if (A[i]+A[i+1])/2 < minAvg:
            minAvg = (A[i]+A[i+1])/2
            minP = i
        if i != len(A)-2:
            if (A[i]+A[i+1]+A[i+2])/3 < minAvg:
                minAvg = (A[i]+A[i+1]+A[i+2])/3
                minP = i 
    return minP