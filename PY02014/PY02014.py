isPrime = [True]*10001

def sieve():
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, 100):
        if isPrime[i]:
            for j in range(2*i, 10001, i):
                isPrime[j] = False
def primeDistance(start, jump):
    for i in range(start, start + 100*jump, jump):
        if isPrime[i]:
            return abs(i - start)
    return 0

sieve()
input()
arr = list(map(int, input().split()))
ans = 0
for ele in arr:
    ans = max(ans, min(primeDistance(ele, -1), primeDistance(ele, 1)))

print(ans)