for test in range(int(input())):
    string1 = sorted(input())
    string2 = sorted(input())
    print(f"Test {test + 1}: ", end= '')
    if string1 == string2:
        print('YES')
    else:
        print('NO')