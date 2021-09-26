P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    pair = input()
    if(pair == "0"):
        break
    pair = pair.split()
    K = int(pair[0])
    string = pair[1]
    ans = []
    for i in string:
        ans.append(P[(P.find(i) + K)%28])
    ans.reverse()
    for i in ans:
        print(i, end='')
    print()