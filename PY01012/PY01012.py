base = input()
string = input()
pos = int(input())

print(base[:pos-1] + string + base[pos-1:])