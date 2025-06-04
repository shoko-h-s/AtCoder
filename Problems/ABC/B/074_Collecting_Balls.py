n = int(input())
k = int(input())
x_list = list(map(int, input().split()))

min_d = 0

for x in x_list:
    a_d = x * 2
    b_d = abs(x-k) * 2
    min_d += min(a_d, b_d)

print(min_d)
