import re

dic = dict()
for line in range(int(input())):
    line = re.findall(r'[A-Za-z]+', input())
    for word in line:
        word = word.lower()
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
for ele in dict(sorted(dic.items(), key= lambda item: (-item[1], item[0]))):
    print(f'{ele} {dic[ele]}')