n = int(input())
arr = set(list(map(int, input().split())))
arr.add(n+2)
# for i, v in enumerate(arr):
#     if v != i+1:
#         print(i+1)
#         break
for i in range(1, n+2):
    if i not in arr:
        print(i)
        break