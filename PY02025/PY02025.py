def printSet(Set):
    for ele in Set:
        print(ele, end=' ')
    print()

ignore = input()
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

printSet(sorted(set1.intersection(set2)))
printSet(sorted(set1.difference(set2)))
printSet(sorted(set2.difference(set1)))