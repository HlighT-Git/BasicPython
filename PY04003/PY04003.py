a, b = input().split()
a, b = int(a), int(b)

import math

c = math.gcd(a, b)
print(f'{a//c}/{b//c}')