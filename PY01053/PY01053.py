for test in range(int(input())):
    num = input()
    sum = 0
    for chr in num:
        sum += int(chr)
    if sum % 3 == 0:
        print('YES')
    else:
        print('NO')