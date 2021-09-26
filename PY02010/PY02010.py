def num(string):
    for i in range(len(string)):
        if string[i] != '0':
            return string[i:]
    return '0'
def theFirstIsBigger(n1, n2):
    if len(n1) == len(n2):
        return n1 > n2
    return len(n1) > len(n2)
while True:
    n = int(input())
    if n == 0:
        break
    havePair = False
    if n == 1:
        ignore = input()
    else:
        min = num(input())
        max = num(input())
        if theFirstIsBigger(min, max):
            min, max = max, min
        for i in range(2, n):
            tmp = num(input())
            if theFirstIsBigger(min, tmp):
                min = tmp
            if theFirstIsBigger(tmp, max):
                max = tmp
        if min != max:
            havePair = [min, max]
    if havePair == False:
        print('BANG NHAU')
    else:
        print(f"{havePair[0]} {havePair[1]}")