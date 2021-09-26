def isPrime(n):
    if n < 2:   
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
def primeSumArr(size):
    res = [0, 2, 5]
    i = 5
    while len(res) < size:
        if(isPrime(i)):
            res.append(res[-1] + i)
        i += 2
    return res

pair = input().split()
n = int(pair[0])
x = int(pair[1])
for i in primeSumArr(n+1):
    print(x + i, end=' ')
