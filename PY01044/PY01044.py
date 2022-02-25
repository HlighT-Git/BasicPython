s1 = set(input().lower().split())
s2 = set(input().lower().split())
for word in sorted(s1.union(s2)):
    print(word, end= ' ')
print()
for word in sorted(s1.intersection(s2)):
    print(word, end= ' ')