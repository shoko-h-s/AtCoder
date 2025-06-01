n = int(input())
a_list = list(map(int, input().split()))

flag = True

for i in range(n-1):
    if a_list[i] >= a_list[i+1]:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
