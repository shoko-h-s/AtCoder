a, b = input().split()

# 桁数が合わない可能性があるので、一の位から計算できるよう反転させる
a_rev = a[::-1]
b_rev = b[::-1]

# ループ回数は桁数が少ない方
times = min(len(a), len(b))

flag = False

for i in range(times):
    if int(a_rev[i]) + int(b_rev[i]) > 9:
        flag = True
        break
        
if flag:
    print("Hard")
else:
    print("Easy")
