input()
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))
if sorted(setA) == sorted(setB):
    print("YES")
else:
    print("NO")