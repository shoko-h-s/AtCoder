n, d = map(int, input().split())

spots = 0

for _ in range(n):
    x, y = map(int, input().split())

    if (x**2 + y**2)**0.5 <= d:
        spots += 1

print(spots)
