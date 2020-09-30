def solution(A):
    # write your code in Python 3.6
    nums = set()
    for n in A:
        if n in nums:
            nums.remove(n)
        else:
            nums.add(n)
    return nums.pop()