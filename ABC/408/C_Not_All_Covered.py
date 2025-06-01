# いもす法を知らなかったため、本番ではACできず（愚直な実装でTLE）
# いもす法を学び、再挑戦したらAC。備忘録として残す。

n, m = map(int, input().split())

# カウント用のリスト
castle_list = [0] * n

# いもす法用のリストを準備
imos_list = [0] * n

for _ in range(m):
    l, r = map(int, input().split())

    # 範囲の始まりのインデックスに +1
    imos_list[l-1] += 1

    # 範囲の終わりの1つ外側のインデックスに -1
    # 配列の外側となる場合は操作不要
    if r < n:
        imos_list[r] -= 1

# カウント用リストの最初は、いもす法用リストの最初の値
castle_list[0] = imos_list[0]

for i in range(1, n):
    # カウント用リストの2つ目以降の処理
    castle_list[i] += castle_list[i-1] + imos_list[i]

print(min(castle_list))
