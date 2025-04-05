a, b = map(int, input().split())

# 必要な数
sockets = b - 1

# 1つあたりの増やせる数
num = a - 1

print((sockets + num - 1) // num)
