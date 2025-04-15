n = int(input())
m_list = [list(map(float, input().split())) for _ in range(n)]

count_list = [0, 0, 0, 0, 0, 0]

for m in m_list:
    if m[0] >= 35:
        count_list[0] += 1
    elif m[0] >= 30:
        count_list[1] += 1
    elif m[0] >= 25:
        count_list[2] += 1
    elif m[0] < 0:
        count_list[5] += 1
        
    if m[1] >= 25:
        count_list[3] += 1
    elif (m[1] < 0) and (m[0] >= 0):
        count_list[4] += 1
        
print(" ".join(map(str, count_list)))
