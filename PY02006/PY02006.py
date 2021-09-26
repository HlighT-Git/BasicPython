def isValid(a, b, length):
    for i in range(length):
        if a[i] > b[i]:
            return False
    return True

test = int(input())
for t in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    if(isValid(a, b, n)):
        print("YES")
    else:
        print("NO")    