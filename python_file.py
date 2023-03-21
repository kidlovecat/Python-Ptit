s = input()
s1 = s[len(s)-3] + s[len(s)-2] + s[len(s)-1]
s2 = s1.lower()
s3 = ".py"
if s2 == s3:
    print("yes")
else:
    print("no")