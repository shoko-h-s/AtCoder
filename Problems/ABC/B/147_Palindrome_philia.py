s = input()

# 文字列を2つに分割
s1 = s[:len(s)//2]

# 文字列の長さの偶奇で、分割方法が変わる
if len(s) % 2 == 0:
    s2 = s[len(s)//2:]
else:
    s2 = s[(len(s)//2) + 1:]

s2 = s2[::-1]
cnt = 0

for i in range(len(s1)):
    if s1[i] != s2[i]:
        cnt += 1

print(cnt)
