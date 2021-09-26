def isLowType(string):
    cnt = 0
    for i in string:
        if i.islower():
            cnt += 1
    if(cnt >= len(string) - cnt):
        return True
    return False

string = input()
if isLowType(string):
    print(string.lower())
else:
    print(string.upper())