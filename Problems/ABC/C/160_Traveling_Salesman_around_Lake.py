k, n = map(int, input().split())
a_list = list(map(int, input().split()))

# 次の番号の家との距離リストを作成
d_list = [abs(a_list[i+1] - a_list[i]) for i in range(n-1)]

# n 番目の家 ～ 1 番目の家の距離を追加
d = a_list[0] + abs(k - a_list[n-1])
d_list.append(d)

# すべての家間距離から、最も長い距離を除いたものが答え
print(sum(d_list) - max(d_list))



# 【備考】
# Training Easy 12
