n = int(input())
p_list = list(map(int, input().split()))

p_max = max(p_list)

if p_max != p_list[0]:
    print(p_max - p_list[0] + 1)
elif p_list.count(p_max) > 1:
    print(1)
else:
    print(0)
