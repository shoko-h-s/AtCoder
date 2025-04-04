import math

# 1 - 10 までの階乗降順リストを作成
f_list = [math.factorial(i+1) for i in range(10)]
f_list = sorted(f_list, reverse=True)

p = int(input())

count = 0

for f in f_list:
    while p >= f:
        p -= f
        count += 1
        
print(count)
