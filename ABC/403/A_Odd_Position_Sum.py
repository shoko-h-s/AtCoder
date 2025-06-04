n = int(input())
a_list = list(map(int, input().split()))

total_a = 0

for i in range(0, n, 2):
    total_a += a_list[i]

print(total_a)
