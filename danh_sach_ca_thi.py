class Ca:
    def __init__(self,ma,ngay,gio,phong):

        ngay = str(ngay)
        gio = str(gio)

        self.ma = 'C{:03d}'.format(ma)
        self.ngay = ngay
        self.gio = gio
        self.phong = phong

        self.day = int(ngay[:2])
        self.month = int(ngay[3:5])
        self.year = int(ngay[6:])
        self.h = int(gio[:2])
        self.m = int(gio[3:])
    def __str__(self):
        return self.ma+' '+ self.ngay+' '+self.gio+' '+self.phong

with open("CATHI.in","r") as file:
    
    ls = []   
    i=1 
    for t in range(int(file.readline())):
        ls.append(Ca(i,file.readline().strip(),file.readline().strip(),file.readline().strip()))
        i+=1
    ls.sort(key=lambda x: (x.year,x.month,x.day,x.h,x.m,x.ma))
    for i in ls:
        print(i)