def solution(A):
    # write your code in Python 3.6
    nums = set([x for x in A if x > 0])
    if len(nums) == 0:
        return 1
    nums = sorted(nums)
    for i,v in enumerate(nums):

        if i + 1 != v:
            return i+1
    return len(nums) + 1