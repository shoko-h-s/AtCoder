k = int(input())

mid_k = k // 2

if k % 2 == 0:
    print(mid_k**2)
else:
    print(mid_k * (mid_k + 1))
