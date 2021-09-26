num = input()
if len(num) % 2 == 1:
    num = num[:-1]
arr = set()
for i in range(0, len(num), 2):
    arr.add(int(num[i:i+2]))

for ele in sorted(arr):
    print(ele, end= ' ')