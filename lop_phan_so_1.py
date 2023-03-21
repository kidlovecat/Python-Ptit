import math
class PhanSo:
    def __init__(self,ts,ms) :
        self.ts = ts
        self.ms = ms
    def compact(self) :
        k = math.gcd(self.ts, self.ms)
        self.ts = int(self.ts / k)
        self.ms = int(self.ms / k)
    def output(self) :
        print(self.ts, "/", self.ms, sep = "")    

if __name__ == '__main__':
    a = input().split()
    ps = PhanSo(int(a[0]),int(a[1]))
    ps.compact()
    ps.output()
