n = input()
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
for i in a:
    if(i in b):
        print(i,end=" ")
print()
for i in a:
    if(i not in b):
        print(i,end=' ')
print()
for i in b:
    if(i not in a):
        print(i,end=' ')