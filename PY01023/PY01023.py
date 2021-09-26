for test in range(int(input())):
    n = int(input())
    print("1", end='')
    i = 2
    while i*i <= n:
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n /= i
            print(f" * {i}^{cnt}", end='')
        i += 1
    if n > 1:
        print(f" * {int(n)}^1", end='')
    print()
