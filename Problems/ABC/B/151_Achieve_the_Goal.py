n, k, m = map(int, input().split())
a_list = list(map(int, input().split()))

scores = sum(a_list)
goal = n * m

if scores >= goal:
    print(0)
    
else:
    target = goal - scores
    
    if target > k:
        print(-1)
        
    else:
        print(target)
