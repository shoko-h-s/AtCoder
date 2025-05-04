n, m = map(int, input().split())
ka_list = [list(map(int, input().split())) for _ in range(n)]

foods = [0] * m

for ka in ka_list:
    k = ka[0]
    
    for i in range(k):
        like_i = ka[i+1]
        foods[like_i-1] += 1
        
print(foods.count(n))
