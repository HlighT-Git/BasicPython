def convert(dec, base):
    res = ""
    while dec > 0:
        char = dec % base
        if char > 9:    char = chr(char + 55)
        res = str(char) + res
        dec //= base
    return res

for test in range(int(input())):
    dec, base = [int(ele) for ele in input().split()]
    print(convert(dec, base))