s = input()
t = input()
miss_flag = True

for i in range(len(s)):
    s = s[-1] + s[:-1]
    
    if s == t:
        print("Yes")
        miss_flag = False
        break
        
if miss_flag:
    print("No")



# 【備考】
# Training Easy 61
