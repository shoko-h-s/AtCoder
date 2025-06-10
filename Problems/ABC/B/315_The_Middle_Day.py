m = int(input())
d_list = list(map(int, input().split()))

middle_day = (sum(d_list) // 2) + 1
total_day = 0

for i in range(m):
    if total_day + d_list[i] < middle_day:
        total_day += d_list[i]
    else:
        ans_m = i + 1
        ans_d = middle_day - total_day

        print(ans_m, ans_d)
        break
