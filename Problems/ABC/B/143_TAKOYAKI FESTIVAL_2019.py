import itertools

n = int(input())
d_list = list(map(int, input().split()))

com_list = list(itertools.combinations(d_list, 2))

total = 0

for com in com_list:
    total += com[0] * com[1]
    
print(total)
