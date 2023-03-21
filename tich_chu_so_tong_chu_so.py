test = int(input())
for i in range(test):
    n = input()
    sum = 0
    mul = 1
    check = 0
    for i in range(len(n)):
        if i % 2 == 1:
            sum += int(n[i])
        else:
            if int(n[i]):
                check = 1
                mul *= int(n[i])
    if check == 0:
        mul = 0
    print(str(mul) + " " + str(sum))