def isPrime(num):
    if num < 2:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True
def isValid(num):
    for i in range(len(num)):
        if isPrime(i):
            if not isPrime(int(num[i])):
                return False
        elif isPrime(int(num[i])):
            return False
    return True

for test in range(int(input())):
    if isValid(input()):
        print('YES')
    else:
        print('NO')