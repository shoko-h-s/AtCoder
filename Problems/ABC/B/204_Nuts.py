n = int(input())
a_list = list(map(int, input().split()))

total = 0

for a in a_list:
    if a > 10:
        total += a - 10
        
print(total)
