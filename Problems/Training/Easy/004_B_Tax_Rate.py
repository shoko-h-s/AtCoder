n = int(input())

flag = False

# 50000程度であれば、全探索が確実
for i in range(1, 50001):
    price = int(i * 1.08)
    
    if price == n:
        print(i)
        flag = True
        break
        
if not flag:
    print(":(")
