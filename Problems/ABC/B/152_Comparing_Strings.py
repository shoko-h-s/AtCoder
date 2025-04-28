a, b = input().split()

s1 = a * int(b)
s2 = b * int(a)

# 辞書順にも min は使用可能
print(min(s1, s2))
