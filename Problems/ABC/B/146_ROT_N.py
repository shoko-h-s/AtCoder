n = int(input())
s = input()

ans = ""

for i in range(len(s)):
    code = ord(s[i]) + n

    if code > ord("Z"):
        code -= 26

    ans += chr(code)

print(ans)
