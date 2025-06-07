n = int(input())
p_list = list(map(int, input().split()))

cnt = 0

for i in range(n):
    if p_list[i] == i+1:
        cnt += 1

# 数とインデックスが対応していない箇所が、2 以下であれば良い
if n - cnt <= 2:
    print("YES")
else:
    print("NO")
