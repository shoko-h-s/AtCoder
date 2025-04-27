n = int(input())
s_list = [input() for _ in range(n)]

s_dict = {}

for s in s_list:
    if s in s_dict:
        print(f"{s}({str(s_dict[s])})")
        s_dict[s] += 1
    else:
        print(s)
        s_dict[s] = 1
