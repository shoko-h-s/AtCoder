n = int(input())

# ケーキとドーナツ、それぞれを買える最大量を求める
cakes = n // 4
donuts = n // 7

success = False

for i in range(cakes+1):
    for j in range(donuts+1):
        total = i * 4 + j * 7
        
        if total == n:
            success = True
            break
                
if success:
    print("Yes")
else:
    print("No")
