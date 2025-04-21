n = int(input())
p_list = list(map(int, input().split()))
q = int(input())
ab_list = [input() for _ in range(q)]

for ab in ab_list:
    a, b = map(int, ab.split())
    
    if p_list.index(a) < p_list.index(b):
        print(a)
    else:
        print(b)
