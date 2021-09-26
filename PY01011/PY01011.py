even = ['0', '2', '4', '6', '8']
validList = []

def init(size, num):
    if len(num) == size/2:
        validList.append(int(num + num[::-1]))
        return
    for digit in even:
        if len(num) != 0 or digit != '0':
            init(size, num + digit)

init(2, '')
init(4, '')
init(6, '')
test = int(input())
for t in range(test):
    n = int(input())
    i = 0
    while i < len(validList) and validList[i] < n:
        print(validList[i], end=' ')
        i += 1
    print()