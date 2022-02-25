def get_int_arr_n_ele(arr):
    n = int(input())
    cnt = n
    while cnt > 0:
        for ele in input().split():
            arr.append(int(ele))
            cnt -= 1

a = []
get_int_arr_n_ele(a)
a.sort()
print(max([a[0] * a[1] * a[-1], a[0] * a[1], a[-2] * a[-1], a[-3] * a[-2] * a[-1]]))