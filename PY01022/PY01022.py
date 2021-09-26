def sumOfDigits(num):
    res = 0
    for digit in num:
        res += ord(digit) - ord('0')
    return str(res)

num = input()
cnt = 0
while len(num) > 1:
    num = sumOfDigits(num)
    cnt += 1
print(cnt)