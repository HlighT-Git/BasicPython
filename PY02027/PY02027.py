import re

ans = []
for line in range(int(input())):
    numbers = re.findall(r'[0-9]+', input())
    for num in numbers:
        ans.append(int(num))
for ele in sorted(ans):
    print(ele)