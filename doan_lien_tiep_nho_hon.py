for j in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    st = [0]
    dp = [1]*1000005
    for i in range(1,n):
        while len(st)>0:
            if a[i]>=a[st[-1]]:
                dp[i] = dp[i]+dp[st[-1]]
                st.pop()
            else:
                break
        st.append(i)
    for i in range(n):
        print(dp[i],end= " ")
    print()