def sum(num):
    string = str(num)
    p = 1
    for i in string:
        p += int(i)
    return p

for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    d = dict()
    for i in arr:
        d[i] = sum(i)
    ans = dict(sorted(d.items(), key = lambda kv:(kv[1], kv[0])))
    for i in ans:
        print(i, end=' ')
    print()