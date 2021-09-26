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
    return isPrime(int(string[:3])) and isPrime(int(string[-3:]))

for test in range(int(input())):
    if isValid(input()):
        print('YES')
    else:
        print('NO')