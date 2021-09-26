def isLess(num):
    for i in range(1, len(num)-1):
        if int(num[i]) < int(num[i-1]):
            return False
    return True

test = int(input())
for t in range(test):
    num = input()
    if isLess(num):
        print("YES")
    else:
        print("NO")