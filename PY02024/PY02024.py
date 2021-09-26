def product(num):
    string = str(num)
    p = 1
    for i in string:
        p *= int(i)
    return p

test = int(input())
for t in range(test):
    n = int(input())
    a = input().split()
    arr = []
    for i in a:
        arr.append(int(i))
    d = dict()
    for i in a:
        d[int(i)] = product(i)
    ans = dict(sorted(d.items(), key = lambda kv:(kv[1], kv[0])))
    for i in ans:
        print(i, end=' ')
    print()