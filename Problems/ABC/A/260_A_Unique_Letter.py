s = input()

flag = False

for i in range(3):
    if s.count(s[i]) == 1:
        print(s[i])
        flag = True
        break

if not flag:
    print(-1)
