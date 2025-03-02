import itertools

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

list_1 = [a, b, c, d, e]

order_list = list(itertools.permutations(list_1))
min_time = 1000

for o in order_list:
    t = 0
    
    for i in range(5):
        if t % 10 == 0:
            t += o[i]
            
        else:
            mod = t % 10
            t += 10 - mod
            t += o[i]
    
    if min_time > t:
        min_time = t
        
print(min_time)



# 【備考】
# Training Easy 38
