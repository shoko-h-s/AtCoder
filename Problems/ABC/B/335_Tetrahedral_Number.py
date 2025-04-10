n = int(input())

# 1つだけn, 残り0のパターンがあるので、n+1 の範囲でループさせる
for x in range(n+1):
    for y in range(n+1):
        for z in range(n+1):
            if x + y + z <= n:
                print(x, y, z)
            else:
                break
