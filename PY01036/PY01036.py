for test in range(int(input())):
    num = int(input())
    sum = 0
    for denominator in range(num%2+2, num+1, 2):
        sum += 1/denominator
    if num%2 == 1:
        sum += 1
    print('{0:.6f}'.format(sum))