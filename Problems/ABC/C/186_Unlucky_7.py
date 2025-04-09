n = int(input())

count = 0

for i in range(1, n+1):
    # 8進数に変換し、プレフィックスを削除
    i_8 = int(oct(i)[2:])
    
    if ("7" not in str(i)) and ("7" not in str(i_8)):
        count += 1
        
print(count)
