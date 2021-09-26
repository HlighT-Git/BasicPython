def biggestSmallerSameDigitsNumberThan(num):
    left = -1
    for i in range(len(num)-1, 0, -1):
        if num[i-1] > num[i]:
            left = i-1
            break
    if left < 0:
        return -1
    right = left+1
    for i in range(left+2, len(num)):
        if num[i] < num[left] and num[i] > num[right]:
            right = i
    if left == 0 and num[right] == '0':
        return -1
    num = list(num)
    num[left], num[right] = num[right], num[left]
    return ''.join(num)

for test in range(int(input())):
    print(biggestSmallerSameDigitsNumberThan(input()))