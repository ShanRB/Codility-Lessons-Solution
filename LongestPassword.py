def validPass(s):
    letters = 0
    digits = 0
    for c in s:
        if c.isdigit():
            digits += 1
        elif c.isalpha():
            letters += 1
        else:
            return False
    return letters % 2 == 0 and digits % 2 == 1
    
def solution(S):
    # write your code in Python 3.6
    maxL = -1
    words = S.split(' ')
    for word in words:
        if validPass(word):
            maxL = max(maxL, len(word))
    return maxL