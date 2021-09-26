arr = []
while len(arr) < 10:
    inp = list(map(int, input().split()))
    arr += [i%42 for i in inp]
print(len(set(arr)))