def isPalindrome(num):
    if num < 10:
        return False
    return str(num) == str(num)[::-1]

n, m = [int(i) for i in input().split()]
arr = []
for line in range(n):
    arr.append([int(i) for i in input().split()])

ans = -1
for row in arr:
    for ele in row:
        if isPalindrome(ele) and ele > ans:
            ans = ele
if ans == -1:
    print("NOT FOUND")
else:
    print(ans)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == ans:
                print(f'Vi tri [{i}][{j}]')