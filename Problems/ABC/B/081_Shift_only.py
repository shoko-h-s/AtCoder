n = int(input())
a_list = list(map(int, input().split()))

count = 0
flag = True

while flag:
    for i in range(n):
        if a_list[i] % 2 == 0:
            a_list[i] //= 2

        else:
            flag = False
            break

        if i == n-1:
            count += 1

print(count)



# 【備考】
# Training Easy 28
