n = int(input())
s = input()

max_x = 0
x = 0

for i in range(n):
    if s[i] == "I":
        x += 1
        
        # 最大値の判定は、x が増加する時のみで良い
        if x > max_x:
            max_x = x
        
    else:
        x -= 1
        
print(max_x)



# 【備考】
# Training Easy 32
