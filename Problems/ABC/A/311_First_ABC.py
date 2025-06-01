n = int(input())
s = input()

a_cnt, b_cnt, c_cnt = 0, 0, 0
i = 0

while (a_cnt == 0) or (b_cnt == 0) or (c_cnt == 0):
    if s[i] == "A":
        a_cnt += 1
    elif s[i] == "B":
        b_cnt += 1
    else:
        c_cnt += 1

    i += 1

print(i)
