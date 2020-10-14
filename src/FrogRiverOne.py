# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    steps = set()
    for i in range(len(A)):
        steps.add(A[i])
        if len(steps) == X:
            return i 
    return -1