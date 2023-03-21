class LichThi:
    def __init__(self, ma, ma_mon, ten_mon, ngay_thi, gio_thi, nhom_thi):
        self.ma = 'T{:03d}'.format(ma)
        self.ma_mon = ma_mon
        self.ten_mon = ten_mon
        self.ngay_thi = ngay_thi
        self.gio_thi = gio_thi
        self.nhom_thi = nhom_thi
        self.ngay = int(self.ngay_thi[:2])
        self.thang = int(self.ngay_thi[3:5])
        self.nam = int(self.ngay_thi[6:])
        self.gio = int(self.gio_thi[:2])
        self.phut = int(self.gio_thi[3:])

    def __str__(self):
        return self.ma + ' ' + self.ma_mon + ' ' + self.ten_mon + ' ' + self.ngay_thi + ' ' + self.gio_thi + ' ' + str(
            self.nhom_thi)


ls_mon = {}
ls_lich_thi = []
n, m = [int(i) for i in input().split()]
for i in range(n):
    ls_mon.update({input(): input()})
for i in range(m):
    arr = input().split()
    ls_lich_thi.append(LichThi(i + 1, arr[0], ls_mon[arr[0]], arr[1], arr[2], arr[3]))
ls_lich_thi.sort(key=lambda x: (x.nam, x.thang, x.ngay, x.gio, x.phut, x.ma_mon))
for i in ls_lich_thi:
    print(i)
