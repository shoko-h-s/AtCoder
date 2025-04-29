s = input()
t = input()

flag = False

for i in range(len(s)):
    if t[i] != s[i]:
        print(i+1)
        flag = True
        break

# 末尾が挿入された文字の場合
if not flag:
    print(len(t))
