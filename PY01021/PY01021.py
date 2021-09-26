for test in range(int(input())):
    string = list(input())
    sum = 0
    string.sort()
    for ele in string:
        if ele < 'A':
            sum += int(ele)
        else:
            print(ele, end= '')
    print(sum)