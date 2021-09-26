def int_split(string, a):
    for i in string:
        a.append(int(string[i]))
    return


size = int(input())
string = input().split()

a = []
int_split(string, a)
ans = 0

for i in range(size-1):
    for j in a[i+1:]:
        if a[i] > j:
            ans += 1

print(ans)