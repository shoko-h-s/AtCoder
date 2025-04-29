n, p = map(int, input().split())
a_list = list(map(int, input().split()))

ap_list = [a for a in a_list if a < p]

print(len(ap_list))
