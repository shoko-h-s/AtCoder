n, d = map(int, input().split())
s = list(input())

s_rev = s[::-1]

for _ in range(d):
    for i in range(n):
        if s_rev[i] == "@":
            s_rev[i] = "."
            break

print("".join(s_rev[::-1]))
