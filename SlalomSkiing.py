def bs(A,l,r,key):
    while(r-l > 1):
        m = l + (r-l)//2
        if A[m] >= key:
            r = m
        else:
            l = m
    return r 

def lsq(A):
    size = len(A)
    tailTable = [0 for _ in range(size+1)]
    tailTable[0] = A[0]
    length = 1
    for i in range(1,size):
        if A[i] < tailTable[0]:
            tailTable[0] = A[i]
        elif A[i] > tailTable[length-1]:
            tailTable[length] = A[i]
            length += 1
        else:
            tailTable[bs(tailTable,0,length-1,A[i])] = A[i]
    return length 

def solution(A):
    bound = max(A) + 1
    matrix = []
    for n in A:
        matrix.append(bound*2 + n)
        matrix.append(bound*2 - n)
        matrix.append(n)
    return lsq(matrix)