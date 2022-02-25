import re

while True:
    try:
        line = input().lower()
        str = re.split('[.|?|!]', line)
        for ele in str:
            s1 = ele.split(',')
            line = ''
            for j, e1 in enumerate(s1):
                s2 = e1.split(':')
                for k, e2 in enumerate(s2):
                    line += e2.strip()
                    if k < len(s2) - 1:
                        line += ': '
                if j < len(s1) - 1:
                    line += ', '
            try:
                line = line.split()
                print(line[0].title(), end='')
                for e in line[1:]:
                    print(' ' + e, end='')
                print()
            except:
                pass
    except EOFError:
        break
           