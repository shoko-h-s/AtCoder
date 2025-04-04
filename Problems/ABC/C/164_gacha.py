n = int(input())

# 集合で入力を受け取り、その要素数が答え
s_list = {input() for _ in range(n)}

print(len(s_list))
