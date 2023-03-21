def check(n):
    cnt = n.count('2')
    if cnt > int(len(n)/2):
        return True
    return False

for t in range(int(input())):
    n = int(input())
    queue = []
    queue.append('1')
    queue.append('2')
    while(n > 0):
        tmp = queue.pop(0)
        if(check(str(tmp))):
            print(tmp, end=' ')
            n -= 1
        queue.append(tmp+'0')
        queue.append(tmp+'1')
        queue.append(tmp+'2')
    print()
        

