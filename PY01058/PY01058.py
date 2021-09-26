def isPrime(num):
    if num < 2:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

for test in range(int(input())):
    if isPrime(int(input()[-4:])):
        print('YES')
    else:
        print('NO')