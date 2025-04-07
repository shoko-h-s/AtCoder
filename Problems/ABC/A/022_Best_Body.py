n, s, t = map(int, input().split())
w = int(input())
a_list = [int(input()) for _ in range(n-1)]

count = 0

for a in a_list:
    if s <= w <= t:
        count += 1
        
    w += a
    
# 最終日の判定が別途必要
if s <= w <= t:
    count += 1
    
print(count)
