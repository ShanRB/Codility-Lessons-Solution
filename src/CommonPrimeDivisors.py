def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def checkPrime(a,b):
    gv = gcd(a,b)
    while (a != 1):
        gva = gcd(a,gv)
        if gva == 1:
            break;
        a //= gva
    if a != 1:
        return False
    while(b != 1):
        gvb = gcd(b,gv)
        if gvb == 1:
            break;
        b //= gvb
    if b != 1:
        return False
    return True
    
def solution(A, B):
    # write your code in Python 3.6
    count = 0
    for i in range(len(A)):
        if checkPrime(A[i],B[i]):
            count += 1
    return count