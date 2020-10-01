def solution(A):
    # write your code in Python 3.6
    elements = {}
    N = len(A)
    for n in A:
        if n in elements:
            elements[n] += 1
        else:
            elements[n] = 1
    
    divisors = {}
    for e in elements.keys():
        divisors[e] = set([1,e])    # init divisors with 1 and itself
    
    maxValue = max(A)
    
    div = 2
    while div*div <= maxValue:
        k = div*div
        while k <= maxValue:
            if k in divisors:
                divisors[k].add(div)
                divisors[k].add(k//div)
            k += div
        div += 1

    result = []
    for n in A:
        result.append(N - sum([elements.get(e,0) for e in divisors[n]]))

    return result
