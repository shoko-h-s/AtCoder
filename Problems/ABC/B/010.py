n = int(input())
a_list = list(map(int, input().split()))

total = 0

for i in range(n):
    
    # 1つ目のパターン、偶数なら1枚追加
    if a_list[i] % 2 == 0:
        total += 1
        a_list[i] -= 1
        
    # 2つ目のパターン、奇数かつ mod 2 以外になるまで操作を続ける
    while (a_list[i] % 3 == 2) or (a_list[i] % 2 == 0):
        total += 1
        a_list[i] -= 1
        
print(total)
