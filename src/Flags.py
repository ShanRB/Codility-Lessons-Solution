def solution(A):
    # write your code in Python 3.6
    size = len(A)
    if size < 3:
        return 0
    peaks = [-1 for _ in range(size)]
    for i in range(size-2,0,-1):
        if A[i] > A[i+1] and A[i] > A[i-1]:
            peaks[i] = i
        else:
            peaks[i] = peaks[i+1]
    peaks[0] = peaks[1]
    i = 1
    result = 0
    while (i * (i-1) <= size):
        pos = 0
        num = 0
        while pos < size and num < i:
            pos = peaks[pos]
            if pos == -1:
                break;
            num += 1
            pos += i
        result = max(result,num)
        i += 1
    return result