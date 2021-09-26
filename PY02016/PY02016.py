def int_split(string, a):
    string = string.split()
    for i in string:
        a.append(int(i))
    return

def most_frequent(List):
    num = dict()
    for i in List:
        if(i in num):
            num[i] += 1
        else:
            num[i] = 1
    val = 0
    counter = 0
    for i in num.keys():
        if counter < num[i]:
            val = i
            counter = num[i]
    return [val, counter]

def most_frequent2(List):
    List.sort()
    List.append(-1)
    val = 0
    tmp = 1
    counter = 0
    for i in range(1, len(List)):
        if List[i] == List[i-1]:
            tmp += 1
        else:
            if tmp > counter:
                val = List[i-1]
                counter = tmp
            tmp = 1
    return [val, counter]


test = int(input())
for t in range(test):
    n = int(input())
    string = input()
    a = []

    int_split(string, a)
    
    ans = most_frequent2(a)
    
    if ans[1] > n/2:
        print(ans[0])
    else:
        print("NO")