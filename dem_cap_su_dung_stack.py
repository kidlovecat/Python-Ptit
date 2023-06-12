from math import* 
n = int(input())
S = []
count = 0

class Data:
    def __init__(self, height, check_behind, the_same):
        self.height = height
        self.check_behind = check_behind
        self.the_same = the_same

def info(h, behind, same):
    return Data(h, behind, same)

for i in range(1, n+1):
    h = int(input())
    TOP = S[-1] if len(S) > 0 else None

    if len(S) == 0:
        S.append(info(h, 0, 0))
    elif len(S) > 0 and TOP.height > h:
        S.append(info(h, 1, 0))
        count += 1
    elif len(S) > 0 and TOP.height == h:
        count += 1
        count += TOP.the_same
        if TOP.check_behind == 1:
            count += 1
        S.append(info(h, TOP.check_behind, TOP.the_same+1))
    elif len(S) > 0 and TOP.height < h:
        while len(S) > 0 and TOP.height < h:
            count += 1
            S.pop()
            if len(S) == 0:
                break
            TOP = S[-1]
        if len(S) > 0:
            TOP = S[-1]
        if len(S) > 0 and TOP.height == h:
            count += 1
            count += TOP.the_same
            if TOP.check_behind == 1:
                count += 1
            S.append(info(h, TOP.check_behind, TOP.the_same+1))
        elif len(S) > 0 and TOP.height > h:
            count += 1
            S.append(info(h, 1, 0))
        else:
            S.append(info(h, 0, 0))

print(count)