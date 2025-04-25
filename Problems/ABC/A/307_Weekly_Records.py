n = int(input())
a_list = list(map(int, input().split()))

week_list = []

for i in range(n):
    week_step = a_list[i*7:i*7+7]
    week_list.append(sum(week_step))
    
print(*week_list)
