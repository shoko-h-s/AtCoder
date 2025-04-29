a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_sum = sum(a_list)
b_sum = sum(b_list)

print(a_sum - b_sum + 1)
