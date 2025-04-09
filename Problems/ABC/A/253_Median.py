a, b, c = map(int, input().split())

if min(a, c) <= b <= max(a, c):
     print("Yes")
else:
    print("No")
