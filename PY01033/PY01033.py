import math

pair = input().split()
left = int(pair[0])
right = int(pair[1])
for first in range(left, right - 1):
    for second in range(first + 1, right):
        for third in range(second + 1, right + 1):
            if math.gcd(first, second) + math.gcd(first, third) + math.gcd(second, third) == 3:
                print(f'({first}, {second}, {third})')