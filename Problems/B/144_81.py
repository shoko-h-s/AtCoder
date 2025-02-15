n = int(input())

success = False

for i in range(1, 10):
    for j in range(1, 10):
        if i * j == n:
            success = True
            break
            
if success:
    print("Yes")
else:
    print("No")
