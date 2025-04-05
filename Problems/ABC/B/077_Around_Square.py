n = int(input())

# n の平方根を小数点切り捨てで求める
n_sqrt = int(n ** 0.5)

# n_sqrt を 2 乗すれば、n 以下の最大の平方数となる
print(n_sqrt ** 2)
