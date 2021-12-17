def isPrime(n):
    if n < 2:   
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

pair = input().split()
n = int(pair[0])
m = int(pair[1])
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
for row in matrix:
    for element in row:
        if isPrime(element):
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()