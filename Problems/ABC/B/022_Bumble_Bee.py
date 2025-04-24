n = int(input())
a_list = [int(input()) for _ in range(n)]

a_set = set(a_list)

print(n - len(a_set))
