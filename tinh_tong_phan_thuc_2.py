t = int(input())
while(t > 0):
    t-=1
    sum = float(0)
    n = int(input())
    if(n % 2 == 0):
        for i in range(2,n+1,2):
            sum += 1.0/i
    else:
        for i in range(1,n+1,2):
            sum += 1.0/i
    print("{:.6f}".format(sum))
    #  print("%.6f" % sum)
    