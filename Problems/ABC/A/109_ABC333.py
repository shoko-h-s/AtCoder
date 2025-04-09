a, b = map(int, input().split())

ab = a * b

if (ab % 2 == 1) or ((ab * 2) % 2 == 1) or ((ab * 3) % 2 == 1):
    print("Yes")
else:
    print("No")
