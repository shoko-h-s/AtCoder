n = int(input())
a_list = list(map(int, input().split()))

a_sorted = sorted(a_list)

print(a_list.index(a_sorted[-2]) + 1)
