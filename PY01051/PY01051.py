for test in range(int(input())):
    num = input()
    sum = 0
    for chr in num:
        sum += int(chr)
    if sum > 9 and str(sum) == str(sum)[::-1]:
        print('YES')
    else:
        print('NO')