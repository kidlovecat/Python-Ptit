for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    cnt = 0
    for i in range(min(a),max(a)+1):
        if(i not in a): 
            cnt +=1
    print(cnt)  