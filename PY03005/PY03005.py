import re

dic = dict()
lines, lim = [int(i) for i in input().split()]
for line in range(lines):
    line = re.findall(r'\w+', input())
    for word in line:
        word = word.lower()
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
for ele in dict(sorted(dic.items(), key= lambda item: (-item[1], item[0]))):
    if dic[ele] >= lim:
        print(f'{ele} {dic[ele]}')