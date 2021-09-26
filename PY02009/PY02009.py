for test in range(int(input())):
    dic = dict()
    for loop in range(int(input())):
        key = int(input())
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 1
    # print(max(dic, key=dic.get))
    # print(sorted(dic.items(), key=lambda kv: (-kv[1], kv[0]))[0][0])
    ans = 1000
    tmp = 0
    for key in dic:
        if dic[key] > tmp:
            tmp = dic[key]
    for key in dic:
        if dic[key] == tmp and key < ans:
            ans = key
    print(ans)