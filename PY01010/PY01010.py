test = int(input())
for t in range(test):
    n = input()
    if(n[:2] == n[-2:]):
        print("YES")
    else:
        print("NO")