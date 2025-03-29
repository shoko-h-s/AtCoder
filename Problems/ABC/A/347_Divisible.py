n, k = map(int, input().split())
a_list = list(map(int, input().split()))

b_list = [a // k for a in a_list if a % k == 0]

print(" ".join(map(str, b_list)))
