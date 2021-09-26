def isLuckyNumber(num):
    for chr in num:
        if chr != '4' and chr != '7':
            return False
    return True

test = int(input())
for t in range(test):
    if(isLuckyNumber(input())):
        print("YES")
    else:
        print("NO")