# Training Easy 8 にも掲載

a, b = input().split()
n = int(a + b)

# 約数の個数を求める → 奇数なら平方数
divisors = [i for i in range(1, n+1) if n % i == 0]

if len(divisors) % 2 == 1:
    print("Yes")
else:
    print("No")
