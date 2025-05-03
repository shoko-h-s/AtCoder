abc_list = list(map(int, input().split()))

abc_list.sort()

# 最大値に他の2数を合わせる
a = abc_list[0]
b = abc_list[1]
max_abc = abc_list[2]

# 小さい2数の偶奇が合う場合
if a % 2 == b % 2:
    answer = max_abc - b
    a += answer

    answer += (max_abc - a) // 2

else:
    b += 1
    max_abc += 1
    answer = 1

    answer += max_abc - b
    a += answer - 1

    answer += (max_abc - a) // 2

print(answer)
