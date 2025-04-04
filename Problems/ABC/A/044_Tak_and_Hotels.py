n = int(input())
k = int(input())
x = int(input())
y = int(input())

if n >= k:
    price = x * k + y * (n - k)
else:
    price = x * n

print(price)
