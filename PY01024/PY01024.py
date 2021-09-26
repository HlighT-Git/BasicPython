def isValid(n):
    for i in range(len(n)-1):
        if abs(ord(n[i]) - ord(n[i+1])) != 2:
            return False
    return True
def sumOfDigits(n):
    res = 0
    for chr in n:
        res += int(chr)
    return res

for test in range(int(input())):
    num = input()
    if isValid(num) and sumOfDigits(num) % 10 == 0:
        print("YES")
    else:
        print("NO")