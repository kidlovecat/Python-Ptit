class TS:
    def __init__(self, ma, ten, maTeam):
        self.ma = f'C{ma:03d}'
        self.ten = ten
        self.tenTeam = dict[maTeam][0]
        self.tenTrg = dict[maTeam][1]

    def toString(self):
        return f'{self.ma} {self.ten} {self.tenTeam} {self.tenTrg}'


ls, dict = [], {}
for i in range(int(input())):
    ma = f'Team{(i + 1):02d}'
    dict[ma] = (input(), input())

for i in range(int(input())):
    ls.append(TS(i + 1, input(), input()))

ls.sort(key=lambda x: x.ten)

for x in ls: print(x.toString())