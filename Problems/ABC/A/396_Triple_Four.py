n = int(input())
a_list = list(map(int, input().split()))

flag = False

for i in range(n-2):
    if a_list[i] == a_list[i+1] == a_list[i+2]:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")
