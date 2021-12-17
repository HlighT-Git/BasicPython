def sumOf2PartOfNum(num):
    size = len(num)
    return str(int(num[:size//2]) + int(num[size//2:]))

num = sumOf2PartOfNum(input())
while True:
    print(num)
    if len(num) == 1:
        break
    num = sumOf2PartOfNum(num)