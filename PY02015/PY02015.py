def done(arr, val):
    for i in arr:
        if i != val:
            return False
    return True

def change(arr):
    res = []
    for i in range(len(arr)-1):
        res.append(abs(arr[i] - arr[i+1]))
    res.append(abs(arr[3] - arr[0]))
    return res


while True:
    arr = list(map(int, input().split()))
    if(done(arr, 0)):
        break
    ans = 0
    while not done(arr, arr[0]):
        arr = change(arr)
        ans += 1
    print(ans)