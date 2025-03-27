n, x = map(int, input().split())
a_list = list(map(int, input().split()))

# x と一致しない要素のみのリストを作る
new_list = [a for a in a_list if a != x]

print(*new_list)
