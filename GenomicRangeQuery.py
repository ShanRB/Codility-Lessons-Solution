def solution(S, P, Q):
    # write your code in Python 3.6
    size = len(S)
    sums = [[0],[0],[0]]
    counts = {'A':[0 for i in range(size+1)],'C':[0 for i in range(size+1)],'G':[0 for i in range(size+1)],'T':[0 for i in range(size+1)]}

    for i in range(0,size):
        for k in counts.keys():
            counts[k][i+1] = counts[k][i]
        counts[S[i]][i+1] += 1
    result = []
    for i in range(len(P)):
        if counts['A'][Q[i]+1] - counts['A'][P[i]] > 0:
            result.append(1)
        elif counts['C'][Q[i]+1] - counts['C'][P[i]] > 0:
            result.append(2)
        elif counts['G'][Q[i]+1] - counts['G'][P[i]] > 0:
            result.append(3)
        else:
            result.append(4)
    return result

if __name__ == '__main__':
    S = 'AC'
    P = [0,1,0]
    Q = [0,1,1]
    
    print(solution(S,P,Q))