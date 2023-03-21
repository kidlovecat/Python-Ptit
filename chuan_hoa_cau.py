import re

while 1==1:
    try:
        s=input()
        s=re.sub('\s+',' ',s)
        if s[-1]!='.' and s[-1]!='?' and s[-1]!='!': 
            s+='.'
        s=s.strip()
        res=''

        for x in s.split():
            if x!='.' and x!='?' and x!='!':
                res+=" "+x
            else:
                res+=x
            if res[-1]=='.' or res[-1]=='?' or res[-1]=='!':
                res=res.strip().capitalize()
                print(res)
                res=''
    except : 
        break