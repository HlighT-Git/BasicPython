num = input()
if len(num) % 2 == 1:
    num = num[:-1]
arr = []

for i in range(0, len(num), 2):
    ele = int(num[i:i+2])
    if ele not in arr:
        arr.append(ele)

for ele in arr:
    print(ele, end= ' ')