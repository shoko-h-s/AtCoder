s = input()

count_list = [s[0]]
flag = True

for i in range(1, len(s)):
    if s[i] in count_list:
        print("no")
        flag = False
        break
        
    else:
        count_list.append(s[i])
        
if flag:
    print("yes")



# 【備考】
# Training Easy 31
