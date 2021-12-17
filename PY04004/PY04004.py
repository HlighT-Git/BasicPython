a, b, c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)

import math

a *= d
c *= b
b *= d
d = math.gcd((a+c), b)

print(f'{(a+c)//d}/{b//d}')
