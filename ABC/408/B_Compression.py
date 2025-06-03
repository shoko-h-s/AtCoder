n = int(input())
a_list = list(map(int, input().split()))

# 重複を除いてソート
a_list = list(set(a_list))
a_list.sort()

print(len(a_list))
print(*a_list)
