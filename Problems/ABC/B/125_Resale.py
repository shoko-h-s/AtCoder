n = int(input())
v_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

max_xy = 0

for i in range(n):
    if v_list[i] > c_list[i]:
        max_xy += v_list[i] - c_list[i]

print(max_xy)
