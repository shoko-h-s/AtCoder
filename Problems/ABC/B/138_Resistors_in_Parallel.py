n = int(input())
a_list = list(map(int, input().split()))

a2_list = [1 / a for a in a_list]
a2_sum = sum(a2_list)

print(1 / a2_sum)
