class Matrix:
    cv = []
    def __init__(self,n,m,arr) :
        self.n = n
        self.m = m
        self.arr = arr
    def chuyenvi(self):
        for i in range(self.m):
            x = []
            for j in range(self.n):
                x.append(a[j][i])
            self.cv.append(x)
        return self.cv
    def mul(self,mx):
        for i in range(self.n) :
            for j in range(self.n) :
                s = 0
                for z in range(self.m) :
                    s += self.arr[i][z] * mx[z][j]
                print(s, end = ' ')
            print()
            
if __name__ == '__main__':
    for t in range(int(input())):
        a = []
        n, m = [int(i) for i in input().split()]
        for i in range(n):
            a.append([int(i) for i in input().split()])
    m = Matrix(n,m,a)
    m.mul(m.chuyenvi())