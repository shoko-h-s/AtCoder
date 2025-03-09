import itertools

# 約数の個数を求める関数
def num_divisor(x):
    list_1 = [i for i in range(1, x+1) if x % i == 0]
    return len(list_1)

n, d = map(int, input().split())
x_list = [list(map(int, input().split())) for _ in range(n)]

count = 0

# 2点の組み合わせを全て挙げる
com_list = list(itertools.combinations(x_list, 2))

for com in com_list:
    num = 0
    
    for i in range(d):
        num += (com[0][i] - com[1][i])**2
    
    # 約数の個数が奇数なら平方数 = 距離が整数となる
    if num_divisor(num) % 2 == 1:
        count += 1
        
print(count)



# 【備考】
# Training Easy 55
