b = int(input())

flag = False

# a の取り得る最大値は 15
for i in range(1, 16):
    if i ** i == b:
        print(i)
        flag = True
        break
        
if not flag:
    print(-1)
