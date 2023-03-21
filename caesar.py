
def encrypt(msg,n):
    msg = str(msg)
    res = ""
    for i in range(len(msg)):
        for j in range(len(chips)):
            if msg[i] == chips[j]:
                
                res += chips[(j+n)%26]
                break
    return res

def decrypt(msg,n):
    msg = str(msg)
    res = ""
    for i in range(len(msg)):
        for j in range(len(chips)):
            if msg[i] == chips[j]:
                res += chips[(j-n)%26]
                break
    return res

chips = [chr(i) for i in range(ord('a'),ord('z')+1)]


for i in range(1,26):
    print(decrypt("krpcfijnzwk",i))
