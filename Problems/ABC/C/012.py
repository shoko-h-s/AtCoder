n = int(input())

# 九九全ての値の和は、2025
answer = 2025 - n

# 答えが answer になる値を全探索
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == answer:
            print(f"{i} x {j}")
