def decode(arr):
    tmp = 'x'
    for c in arr:
        if c >= '0' and c <= '9':
            for i in range(int(c)):
                print(tmp, end='')
        else:
            tmp = c
    return

test = int(input())
for t in range(test):
    arr = input()
    decode(arr)
    print()