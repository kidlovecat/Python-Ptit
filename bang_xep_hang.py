dct = {}
for t in range(int(input())):
    ten = input()
    a = [int(i) for i in input().split()]
    dct[ten] = [a[0], a[1]]
ls = list(dct.keys())
ls.sort(key=lambda x: (-dct[x][0],dct[x][1],x))
for i in ls:
    print('{} {} {}'.format(i,dct[i][0],dct[i][1]))
