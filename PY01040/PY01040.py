def devide(string):
    size = len(string)
    return string[:size//2], string[size//2:]

def rotateChar(char, time):
    char = (ord(char) - ord('A')) + time
    return chr(char%26 + ord('A'))
def rotate(string):
    string = list(string)
    rotDeg = 0
    for ele in string:
        rotDeg += ord(ele) - ord('A')
        rotDeg %= 26
    for i in range(len(string)):
        string[i] = rotateChar(string[i], rotDeg)
    return ''.join(string)
def merge(string, encode):
    string = list(string)
    for i in range(len(string)):
        string[i] = rotateChar(string[i], ord(encode[i]) - ord('A'))
    return ''.join(string)

for test in range(int(input())):
    left, right = devide(input())
    print(merge(rotate(left), rotate(right)))