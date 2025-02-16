list_1 = list(map(int, input().split()))

if (list_1.count(5) == 2) and (list_1.count(7) == 1):
    print("YES")
else:
    print("NO")
