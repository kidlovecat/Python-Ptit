class Phim:
    def __init__(self, ma, the_loai, ngay_chieu, ten, so_tap):
        self.ma = 'P{:03d}'.format(ma)
        self.the_loai = the_loai
        self.ngay_chieu = ngay_chieu
        self.ten = ten
        self.so_tap = so_tap

    def getngay(self):
        return int(self.ngay_chieu[:2])

    def getthang(self):
        return int(self.ngay_chieu[3:5])

    def getnam(self):
        return int(self.ngay_chieu[6:])

    def __str__(self):
        return self.ma + ' ' + self.the_loai + ' ' + self.ngay_chieu + ' ' + self.ten + ' ' + str(self.so_tap)


n, m = [int(i) for i in input().split()]
ls_the_loai = ['0']
ls_phim = []
for i in range(n):
    ls_the_loai.append(input())
for i in range(m):
    ls_phim.append(Phim(i + 1, ls_the_loai[int(input()[2:])], input(), input(), int(input())))
ls_phim.sort(key=lambda x: (x.getnam(), x.getthang(), x.getngay(), x.ten, -x.so_tap))
for i in ls_phim:
    print(i)
