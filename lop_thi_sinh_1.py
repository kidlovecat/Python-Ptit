class ThiSinh:
    def __init__(self,ten,ns,p1,p2,p3) :
        self.ten = ten
        self.ns = ns
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def output(self):
        print('{} {} {:.1f}'.format(self.ten,self.ns,self.p1+self.p2+self.p3))

if __name__ == '__main__':
    ts = ThiSinh(input(),input(),float(input()),float(input()),float(input()))
    ts.output()