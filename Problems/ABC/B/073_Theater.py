n = int(input())
a_list = [list(map(int, input().split())) for i in range(n)]

total = 0

for a in a_list:
    total += a[1] - a[0] + 1
    
print(total)
