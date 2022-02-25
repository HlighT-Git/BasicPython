seen = {}
n = int(input())
end = 1
while True:
    if n < 1:
        break
    for ckey in input().split():
        seen[int(ckey)] = True
        end = max(end, int(ckey))
        n -= 1
flag = True
for num in range(1, end):
    if not seen.get(num):
        flag = False
        print(num)
if flag:
    print('Excellent!')