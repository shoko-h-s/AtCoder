h, n = map(int, input().split())
a_list = list(map(int, input().split()))

if h <= sum(a_list):
    print("Yes")
else:
    print("No")
