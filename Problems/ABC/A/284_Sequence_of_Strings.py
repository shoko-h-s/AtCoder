n = int(input())
s_list = [input() for _ in range(n)]

s_rev = s_list[::-1]

for s in s_rev:
    print(s)
