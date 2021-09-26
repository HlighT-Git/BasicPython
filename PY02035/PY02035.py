num = input()
lim = int(input())
if len(num) % 2 == 1:
    num = num[:-1]
arr = {}

for i in range(0, len(num), 2):
    ele = int(num[i:i+2])
    if ele in arr:
        arr[ele] += 1
    else:
        arr[ele] = 1

ans = []
for key in arr:
    if arr[key] >= lim:
        ans.append(f'{key} {arr[key]}')
if ans:
    for ele in sorted(ans):
        print(ele)
else:
    print("NOT FOUND")