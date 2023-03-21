import math
class PhanSo:
    def __init__(self,ts,ms) :
        self.ts = ts
        self.ms = ms
    def compact(self) :
        k = math.gcd(self.ts, self.ms)
        self.ts = int(self.ts / k)
        self.ms = int(self.ms / k)
    def add(self, x) :
        a = self.ts * x.ms + x.ts * self.ms
        b = self.ms * x.ms
        self.ts = a
        self.ms = b
    def output(self) :
        print(self.ts, "/", self.ms, sep = "") 
    
if __name__ == '__main__':
    a, b, c, d = [int(i) for i in input().split()]
    ps1 = PhanSo(a,b)
    ps2 = PhanSo(c,d)
    ps1.add(ps2)
    ps1.compact()
    ps1.output()