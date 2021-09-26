def solve(num, base):
    if num not in base:
        base.append(int(num))
    if num == 1:
        return len(base)
    if num&1 == 0:
        num /= 2
    else:
        num = num*3 + 1
    return solve(int(num), base)

while True:
    num = int(input())
    if(num == 0):
        break
    print(solve(num, []))