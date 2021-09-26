num = input()
if len(num) % 2 == 1:
    num = num[:-1]
arr = {}

for i in range(0, len(num), 2):
    ele = int(num[i:i+2])
    if ele in arr:
        arr[ele] += 1
    else:
        arr[ele] = 1

for key in arr:
    print(f'{key} {arr[key]}')