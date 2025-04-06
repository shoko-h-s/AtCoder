n = int(input())

# 年齢を保持するために辞書、出力用にリストを作成
sa_dict = {}
s_list = []

for _ in range(n):
    s, a = input().split()
    a = int(a)
    sa_dict[s] = a
    s_list.append(s)
    
# 年齢が最小の人物を抽出、リストでのインデックスを取得
min_person = min(sa_dict, key = sa_dict.get)
i = s_list.index(min_person)

for _ in range(n):
    print(s_list[i])
    
    # 次の人物へ進める、インデックスが末尾となっている場合は先頭に戻す
    if i == n-1:
        i = 0
    else:
        i += 1
