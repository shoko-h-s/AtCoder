n = int(input())
ab_list = [list(map(int, input().split())) for _ in range(n)]

total = 0

for ab in ab_list:
    a = ab[0]
    b = ab[1]
    num = b - a + 1
    
    # 等差数列の和の公式を用いる
    # Sn = 1/2n(a+l)
    total += ((a + b) * num) // 2
    
print(total)
