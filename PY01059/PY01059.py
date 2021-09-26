def sum(start, jump, num):
    res = 0
    for chr in num[start::jump]:
        res += int(chr)
    return res

def product(start, jump, num):
    if sum(start, jump, num) == 0:
        return 0
    res = 1
    for chr in num[start::jump]:
        if int(chr) != 0:
            res *= int(chr)
    return res

for test in range(int(input())):
    num = input()
    print(f'{sum(0, 2, num)} {product(1, 2, num)}')