se_list = [list(map(int, input().split())) for i in range(3)]

score = 0

for se in se_list:
    s = se[0]
    e = se[1]
    
    score += int(s * e * 0.1)
    
print(score)
