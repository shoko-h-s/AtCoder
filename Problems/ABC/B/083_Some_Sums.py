def d_sum(x):
    d_total = 0

    while x > 0:
        d_total += x % 10
        x //= 10

    return d_total


n, a, b = map(int, input().split())

numbers = []
total = 0

for i in range(1, n+1):
    judge = d_sum(i)

    if a <= judge <= b:
        total += i

print(total)
