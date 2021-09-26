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
    num = input()
    sum = 0
    for chr in num:
        sum += int(chr)
    if isPrime(sum):
        print('YES')
    else:
        print('NO')