n = int(input())
a_list = list(map(int, input().split()))

a_list = list(set(a_list))
a_sorted = sorted(a_list)

print(a_sorted[-1] - a_sorted[0])
