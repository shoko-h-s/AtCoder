import math

n = int(input())
r_list = [int(input()) for _ in range(n)]

r_sorted = sorted(r_list, reverse=True)

num = 0

for i in range(n):
    if i % 2 == 0:
        num += r_sorted[i] ** 2
    else:
        num -= r_sorted[i] ** 2
        
print(num * math.pi)
