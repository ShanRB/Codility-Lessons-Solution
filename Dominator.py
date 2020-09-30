def solution(A):
    # write your code in Python 3.6
    if not A:
        return -1
    count = 0
    value = None
    index = 0
    for i in range(len(A)):
        if count == 0:
            value = A[i]
            count += 1
            index = i 
        else:
            if A[i] == value:
                count += 1
            else:
                count -= 1
                if count == 0:
                    value = A[i]
                    index = i 
    if count == 0:
        return -1
    count = 0
    for n in A:
        if n == value:
            count += 1
    if count > len(A)/2:
        return index
    return -1

if __name__ == '__main__':
    A = [1,2,2,1,1,2,2]
    print(solution(A))