n = int(input())
w_list = [input() for _ in range(n)]

success_flag = True

for i in range(1, n):
    before_word = w_list[i-1]
    after_word = w_list[i]
    
    if before_word[-1] != after_word[0]:
        print("No")
        success_flag = False
        break
        
    if w_list[:i].count(w_list[i]) > 0:
        print("No")
        success_flag = False
        break
        
if success_flag:
    print("Yes")



# 【備考】
# Training Easy 54
