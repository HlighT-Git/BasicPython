for test in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    seen = []
    for ele in arr:
        if ele in seen:
            seen.remove(ele)
        else:
            seen.append(ele)
    print(seen[0])