n, m = map(int, input().split())
a_list = list(map(int, input().split()))

if n >= sum(a_list):
    print(n - sum(a_list))
else:
    print(-1)
