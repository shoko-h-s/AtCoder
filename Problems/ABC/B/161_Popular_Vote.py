n, m = map(int, input().split())
a_list = list(map(int, input().split()))

a_sorted = sorted(a_list, reverse=True)

value = sum(a_list) * (1 / (4 * m))

if a_sorted[m-1] >= value:
     print("Yes")
else:
    print("No")
