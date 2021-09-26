n = int(input())

odd = []
even = []
arr = []

while len(arr) < n:
    arr += list(map(int, input().split()))

for num in arr:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

odd.sort(reverse=True)
even.sort()

i, j = 0, 0
for num in arr:
    if num % 2 == 0:
        print(even[i], end=' ')
        i += 1
    else:
        print(odd[j], end=' ')
        j += 1