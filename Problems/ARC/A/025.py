d_list = list(map(int, input().split()))
j_list = list(map(int, input().split()))

gold = 0

for i in range(7):
    if d_list[i] >= j_list[i]:
        gold += d_list[i]
    else:
        gold += j_list[i]
        
print(gold)
