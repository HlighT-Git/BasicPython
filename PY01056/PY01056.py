def isPrime(num):
    if num < 2:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True
def isValid(string):
    sum = 0
    mod = 1
    for chr in string:
        if int(chr) % 2 == mod:
            return False
        sum += int(chr)
        mod = 1 - mod
    return isPrime(sum)

for test in range(int(input())):
    if isValid(input()):
        print('YES')
    else:
        print('NO')