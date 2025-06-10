n, k = map(int, input().split())
s_list = [input() for _ in range(k)]

s_list.sort()

for s in s_list:
    print(s)
