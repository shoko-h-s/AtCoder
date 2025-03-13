n, m = map(int, input().split())
ps_list = [input() for _ in range(m)]

# 各問題の提出記録、問題番号とリストを合わせる
problems = [[None, 0] for _ in range(n+1)]

ac_count = 0
wa_count = 0

for ps in ps_list:
    p, s = ps.split()
    p = int(p)
    
    # 初めて提出した問題
    if problems[p][0] == None:
        if s == "AC":
            problems[p][0] = "AC"
            problems[p][1] = 1
            ac_count += 1
            
        else:
            problems[p][0] = "WA"
            problems[p][1] = 1
    
    # WA を出したことがある問題
    elif problems[p][0] == "WA":
        if s == "AC":
            problems[p][0] = "AC"
            wa_count += problems[p][1]
            
            problems[p][1] += 1
            ac_count += 1
            
        else:
            problems[p][1] += 1
            
    # 既に AC を出した問題は処理不要
            
print(ac_count, wa_count)



# 【備考】
# Training Easy 76
