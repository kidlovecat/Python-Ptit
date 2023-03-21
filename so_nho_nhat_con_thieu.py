n = input() 
arr = [int(i) for i in input().split()] 
print(min([i for i in range(1,max(arr)+2) if i not in arr]))