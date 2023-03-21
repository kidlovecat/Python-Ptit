class SV:
    rank = 1

    def __init__(self, ma, ten, d1, d2, d3):
        self.ma = 'SV{:02d}'.format(ma)
        tmp = ten.lower().split()
        for i in range(len(tmp)):
            tmp[i] = tmp[i][0].upper() + tmp[i][1:]
        self.ten = ' '.join(tmp)

        value = int(((d1 * 3 + d2 * 3 + d3 * 2) / 8) * 100 + 0.5)
        value /= 100
        self.diem = value

    def __str__(self):
        return self.ma + ' ' + self.ten + ' {:.2f} '.format(self.diem) + str(self.rank)


ls = []

for i in range(int(input())):
    ls.append((SV(i + 1, input(), float(input()), float(input()), float(input()))))
ls.sort(key=lambda x: (-x.diem, x.ma))
for i in range(1, len(ls)):
    ls[i].rank = ls[i - 1].rank if ls[i].diem == ls[i - 1].diem else i + 1
for i in ls:
    print(i)
