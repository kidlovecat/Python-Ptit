import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, k) :
        x0 = self.x - k.x
        y0 = self.y - k.y
        return math.sqrt(x0 * x0 + y0 * y0)
class Triangle:
    def __init__(self,p1,p2,p3) :
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def output(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)
        if(max(a,b,c)*2 >= (a+b+c)): 
            print('INVALID')
        else:
            print('{:.2f}'.format(0.25*math.sqrt((a+b+c)*(a+b-c)*(b+c-a)*(c+a-b))))

for x in range(int(input())):
    a = [float(i) for i in input().split()]
    triagle = Triangle(Point(a[0], a[1]), Point(a[2], a[3]), Point(a[4], a[5]))
    triagle.output()