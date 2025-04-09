n = int(input())
a_list = list(map(int, input().split()))

a_sorted = sorted(a_list)

for i in range(n-1):
    
    # 前後の数値差が1にならない部分が抜けている個所
    if a_sorted[i+1] - a_sorted[i] != 1:
        print(a_sorted[i] + 1)
        break
