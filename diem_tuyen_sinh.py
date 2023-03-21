kv = [0, 1.5, 1, 0]


class ThiSinh:
    def __init__(self, ma, ten, diem, dan_toc, khu_vuc):
        self.ma = 'TS{:02d}'.format(ma)
        tmp = ten.lower().split()
        for i in range(len(tmp)):
            tmp[i] = tmp[i][0].upper() + tmp[i][1:]
        self.ten = ' '.join(tmp)
        self.dan_toc = dan_toc
        self.khu_vuc = khu_vuc
        if dan_toc == 'Kinh':
            self.diem = diem + kv[int(khu_vuc)]
        else:
            self.diem = diem + kv[int(khu_vuc)] + 1.5
        if self.diem >= 20.5:
            self.trang_thai = 'Do'
        else:
            self.trang_thai = 'Truot'

    def __str__(self):
        return self.ma + ' ' + self.ten + ' ' + '{:.1f}'.format(self.diem) + ' ' + self.trang_thai


ls_ts = []
n = int(input())
for i in range(n):
    ls_ts.append((ThiSinh(i + 1, input(), float(input()), input(), input())))
ls_ts.sort(key=lambda x: (-x.diem, x.ma))
for i in ls_ts:
    print(i)
