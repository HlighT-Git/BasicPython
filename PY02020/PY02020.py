n = int(input())
arr = list(map(float, input().split()))
arr = [ele for ele in arr if ele != max(arr) and ele != min(arr)]
print('{0:.2f}'.format(sum(arr)/len(arr)))