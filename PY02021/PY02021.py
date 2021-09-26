for test in range(int(input())):
    len1, len2, len3 = [int(i) for i in input().split()]
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr3 = list(map(int, input().split()))
    ans = []
    i, j, k = 0, 0, 0
    while i < len1 and j < len2 and k < len3:
        if arr1[i] == arr2[j] == arr3[k]:
            ans.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    if ans:
        for ele in ans:
            print(ele, end=' ')
        print()
    else:
        print("NO")