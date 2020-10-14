def solution(A):
    # write your code in Python 3.6
    lastWall = 0
    currDepth = 0
    maxDepth = 0
    bottom = 0
    for n in A:
        if n >= lastWall:
            currDepth = 0
            maxDepth = max(maxDepth, lastWall - bottom)
            bottom = n
            lastWall = n
        elif n > bottom:
            maxDepth = max(maxDepth, n - bottom)
        else:
            bottom = n

    return maxDepth

if __name__ == '__main__':
    A = [2,1,3]
    print(solution(A))