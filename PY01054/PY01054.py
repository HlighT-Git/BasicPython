for test in range(int(input())):
    num = input()
    prd = 1
    for chr in num:
        if chr != '0':
            prd *= int(chr)
    print(prd)