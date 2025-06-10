s_list = input().split("|")

ans_list = []

for s in s_list:
    if len(s) > 0:
        ans_list.append(s.count("-"))

print(*ans_list)
