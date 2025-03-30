n, k, x = map(int, input().split())
a_list = list(map(int, input().split()))

a_list.insert(k, x)

print(" ".join(map(str, a_list)))
