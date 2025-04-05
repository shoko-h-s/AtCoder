n, k = map(int, input().split())

total = 0

for i in range(n):
    for j in range(k):
        room = int(str(i+1) + "0" + str(j+1))
        total += room
        
print(total)
