class KH:
    def __init__(self, ma, ten, loai, dau, cuoi):
        self.ma = f'KH{ma:02d}'
        self.ten = " ".join(ten.lower().strip().title().split())

        if loai == "A":
            self.dm = 100
        elif loai == "B":
            self.dm = 500
        else:
            self.dm = 200

        x = cuoi - dau
        self.tienDm = (x * 450 if x < self.dm else self.dm * 450)

        self.vuotDm = ((x - self.dm) * 1000 if x > self.dm else 0)

        self.vat = self.vuotDm // 20

        self.tong = self.tienDm + self.vuotDm + self.vat

    def toString(self):
        return f'{self.ma} {self.ten} {self.tienDm} {self.vuotDm} {self.vat} {self.tong}'


ls = []
for i in range(int(input())):
    ten = input()
    a = input().split()
    ls.append(KH(i + 1, ten, a[0], int(a[1]), int(a[2])))

ls.sort(key=lambda x: -x.tong)

for x in ls: print(x.toString())