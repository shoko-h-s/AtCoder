n = int(input())

total = 0

for i in range(n):
    total += (i+1) * 10000

print(total * (1 / n))
