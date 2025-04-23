n = int(input())
a_list = list(map(int, input().split()))

a_sorted = sorted(a_list, reverse=True)
a_max_2 = a_sorted[1]
i = a_list.index(a_max_2)

print(i+1)
