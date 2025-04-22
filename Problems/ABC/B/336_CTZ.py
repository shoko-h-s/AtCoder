n = int(input())

# 2進数変換して、逆順にする
n2 = bin(n)
n2_rev = n2[::-1]

count = 0
i = 0

while n2_rev[i] == "0":
    count += 1
    i += 1
    
print(count)
