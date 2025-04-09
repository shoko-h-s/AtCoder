n, s, k = map(int, input().split())
pq_list = [list(map(int, input().split())) for _ in range(n)]

price = 0

for pq in pq_list:
    price += pq[0] * pq[1]
    
if price < s:
    price += k
    
print(price)
