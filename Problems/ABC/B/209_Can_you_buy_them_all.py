n, x = map(int, input().split())
a_list = list(map(int, input().split()))

a2_list = [a_list[i] - 1 if i % 2 == 1 else a_list[i] for i in range(n)]

if x >= sum(a2_list):
    print("Yes")
else:
    print("No")
