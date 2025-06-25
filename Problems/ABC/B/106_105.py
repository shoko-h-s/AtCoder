# 約数の個数を求める関数
def num_divisor(x):
    list_1 = [i for i in range(1, x+1) if x % i == 0]
    return len(list_1)

n = int(input())

count = 0

# 奇数のみチェックする
for i in range(1, n+1, 2):
    if num_divisor(i) == 8:
        count += 1

print(count)
