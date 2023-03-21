s = input()

cnt = sum(1 for c in s if c.islower())

if(cnt >= len(s)/2): print(s.lower())
else: print(s.upper())