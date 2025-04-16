# 文字列をスワップする場合は、一旦リスト化した方が便利
s_list = list(input())
a, b = map(int, input().split())

s_list[a-1], s_list[b-1] = s_list[b-1], s_list[a-1]

print("".join(s_list))
