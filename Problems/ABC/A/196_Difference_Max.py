a, b = map(int, input().split())
c, d = map(int, input().split())

max_number = -200

for i in range(a, b+1):
    for j in range(c, d+1):
        n = i - j
        max_number = max(max_number, n)
        
print(max_number)
