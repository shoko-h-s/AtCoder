n = int(input())
a_list = list(map(int, input().split()))

sum_a = sum(a_list)

# 全員の合計値を符号反転させたものが答え
print(sum_a * (-1))
