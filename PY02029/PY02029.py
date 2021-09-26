n, m = [int(i) for i in input().split()]
cnt = [0]*m

for id in input().split():
    cnt[int(id)-1] += 1

tmp = [ele for ele in cnt if ele != max(cnt)]
if tmp and max(tmp) != 0:
    print(cnt.index(max(tmp)) + 1)
else:
    print("NONE")