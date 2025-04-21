s = input()

if s.count("a") == 0:
    print(-1)

# 検索文字が最後に現れるインデックスを取得 → str.rfind
else:
    print(s.rfind("a") + 1)
