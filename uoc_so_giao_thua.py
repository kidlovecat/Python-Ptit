for t in range(int(input())):
	dem=0
	n,p=input().split()
	n = int(n)
	p = int(p)
	for i in range(2,n+1):
		x=i	
		while x%p==0:
			dem+=1
			x//=p
	print(dem)