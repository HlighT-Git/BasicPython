def encode(arr):
    tmp = arr[0]
    cnt = 1
    res = ''
    for c in arr[1:]:
        if c == tmp:
            cnt += 1
        else:
            res += f"{cnt}{tmp}"
            tmp = c
            cnt = 1
    res += f"{cnt}{tmp}"
    return res

test = int(input())
for t in range(test):
    arr = input()
    arr = encode(arr)
    print(arr)