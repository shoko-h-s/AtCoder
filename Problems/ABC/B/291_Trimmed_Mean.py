n = int(input())
x_list = list(map(int, input().split()))

x_list.sort()
x_list = x_list[n:-n]

print(sum(x_list) / (3*n))
