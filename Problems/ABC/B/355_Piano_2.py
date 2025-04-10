n, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

c_list = a_list + b_list
c_sorted = sorted(c_list)

flag = False

for i in range(n+m-1):
    if (c_sorted[i] in a_list) and (c_sorted[i+1] in a_list):
        flag = True
        break
        
if flag:
    print("Yes")
else:
    print("No")
