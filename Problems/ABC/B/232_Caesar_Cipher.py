s = input()
t = input()

k = ord(t[0]) - ord(s[0])

if k < 0:
    k += 26

flag = True

for i in range(1, len(s)):
    code = ord(s[i]) + k
    if code > ord("z"):
        code -= 26

    if code != ord(t[i]):
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
