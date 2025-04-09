n = int(input())
a_list = list(map(int, input().split()))

total = 0

for a in a_list:
    total += a
    
print(total)
