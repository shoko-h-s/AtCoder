n = int(input())
d, x = map(int, input().split())
a_list = [int(input()) for _ in range(n)]

total = x

# 各自が食べた数 = 日数を a で切り上げ除算した答え
for a in a_list:
    total += (d + a - 1) // a
    
print(total)
