a, b, c = map(int, input().split())

# 安い方のみを可能な限り買うのが最適解
print(c // min(a, b))
