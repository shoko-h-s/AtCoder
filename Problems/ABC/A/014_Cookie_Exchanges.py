a, b, c = map(int, input().split())

count = 0

if (a == b == c) and (a % 2 == 0):
    print(-1)

elif (a % 2 == 1) or (b % 2 == 1) or (c % 2 == 1):
    print(0)

else:    
    while True:
        tmp_a = a
        tmp_b = b
        tmp_c = c

        a = tmp_b // 2 + tmp_c // 2
        b = tmp_a // 2 + tmp_c // 2
        c = tmp_a // 2 + tmp_b // 2
        count += 1

        if (a % 2 == 1) or (b % 2 == 1) or (c % 2 == 1):
            break
            
    print(count)



# 【備考】
# Training Easy 13 にも掲載
