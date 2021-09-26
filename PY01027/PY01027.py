def isValidNum(num):
    i = 0
    while i < len(num):
        jump = 1
        if num[i:i+3] == '688':
            jump = 3
        elif num[i:i+2] == '68':
            jump = 2
        elif num[i] != '6':
            return False
        i += jump
    return True

if isValidNum(input()):
    print("YES")
else:
    print("NO")