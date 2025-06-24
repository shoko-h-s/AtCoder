n = int(input())
t = input()
a = input()

flag = False

for i in range(n):
    if t[i] == a[i] == "o":
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")
