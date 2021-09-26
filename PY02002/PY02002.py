fibo = [1]*93
fibo[0] = 0
for i in range(3, 93):
    fibo[i] = fibo[i-1] + fibo[i-2]

test = int(input())
for t in range(test):
    pair = input().split()
    for i in range(int(pair[0]), int(pair[1])+1):
        print(fibo[i], end= ' ')
    print()