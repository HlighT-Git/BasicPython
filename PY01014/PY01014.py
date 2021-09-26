inp = list(map(int, input().split()))
a = inp[0]
K = inp[1]
N = inp[2]

sum = (int(a/K)+1)*K

if(sum > N):
    print(-1)
else:
    while sum <= N:
        print(sum - a, end= ' ')
        sum += K