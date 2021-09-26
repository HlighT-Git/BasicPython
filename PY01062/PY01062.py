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
    cnt = 0
    for ele in string:
        if isPrime(int(ele)):
            cnt += 1
    return cnt > len(string) - cnt and isPrime(int(len(string)))

for test in range(int(input())):
    if isValid(input()):
        print('YES')
    else:
        print('NO')