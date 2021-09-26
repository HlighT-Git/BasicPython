test = int(input())

def round(num):
    if num < 5:
        return 0
    return 1

for t in range(test):
    revAns = ""
    num = input()
    remember = 0
    for chr in num[:0:-1]:
        revAns += '0'
        remember = round(int(chr) + remember)
    revAns += str(int(num[0]) + remember)[::-1]
    print(revAns[::-1])