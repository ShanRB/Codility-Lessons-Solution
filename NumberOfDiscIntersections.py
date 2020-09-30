def solution(A):
    # write your code in Python 3.6
    disks = []
    for i,v in enumerate(A):
        disks.append((i-v,1))
        disks.append((i+v,0))
    disks.sort(key=lambda x: (x[0], not x[1]))
    active = 0
    intersections = 0
    for i,isBegin in disks:
        if isBegin:
            intersections += active
            active += 1
        else:
            active -= 1
        if intersections > 10**7:
            return -1
    return intersections