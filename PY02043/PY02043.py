for test in range(int(input())):
    string = input()
    num = input()
    newString = string.replace(num, '', string.count(num))
    print(string.count(num)*len(num))