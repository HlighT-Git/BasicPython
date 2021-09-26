import math

for test in range(int(input())):
    num = input()
    if math.gcd(int(num), int(num[::-1])) == 1:
        print('YES')
    else:
        print('NO')