n, c1, c2 = input().split()
s = input()

ans = ""

for i in range(len(s)):
    if s[i] == c1:
        ans += c1
    else:
        ans += c2

print(ans)
