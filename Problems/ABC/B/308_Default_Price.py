n, m = map(int, input().split())
c_list = list(input().split())
d_list = list(input().split())
p_list = list(map(int, input().split()))

price = 0

for c in c_list:
    if c in d_list:
        i = d_list.index(c) + 1
        price += p_list[i]
        
    else:
        price += p_list[0]
        
print(price)
