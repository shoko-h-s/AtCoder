a, b, c = map(int, input().split())

if b + c <= a:
    print(0)
else:
    print(c - (a - b))
