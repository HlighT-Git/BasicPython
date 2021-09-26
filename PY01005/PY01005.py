string = input()
cnt = string.count('4') + string.count('7')
if cnt == 4 or cnt == 7:
    print("YES")
else:
    print("NO")