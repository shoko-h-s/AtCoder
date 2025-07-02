s = input()
t = input()

if s == t:
    print(0)
else:
    flag = True

    n = min(len(s), len(t))

    for i in range(n):
        if s[i] != t[i]:
            print(i+1)
            flag = False
            break

    if flag:
        print(n+1)
