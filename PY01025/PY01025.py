num = input()
num = num[::-1]
tmp = ''
for index, chr in enumerate(num):
    if index % 3 == 0:
        tmp += ','
    tmp += chr
print(tmp[:0:-1])