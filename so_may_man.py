str = input()
cnt = 0
for i in range(0, len(str), 1):
    if int(str[i]) == 4 or int(str[i]) == 7: cnt+=1
    
if(cnt == 4 or cnt == 7): print("YES")
else: print("NO")

#so may man 2
# t = int(input())
# while t > 0:
#     t-=1
#     check = 0
#     s = input()
#     for i in range (len(s)):
#         if(s[i] != '4' and s[i] != '7'): 
#             print("NO")
#             check = 1
#             break
#     if check == 0 : print("YES")
            
