l, h = map(int, input().split())
n = int(input())
a_list = [int(input()) for _ in range(n)]

for a in a_list:
    if a < l:
        print(l - a)
    elif a <= h:
        print(0)
    else:
        print(-1)
