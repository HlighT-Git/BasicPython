def isValid(string):
    if len(string) % 2 == 0:
        return False
    if string[0] == string[1]:
        return False
    base = string[0]
    for i in range(2, len(string), 2):
        if string[i] != base:
            return False
    return True

for test in range(int(input())):
    if isValid(input()):
        print('YES')
    else:
        print('NO')