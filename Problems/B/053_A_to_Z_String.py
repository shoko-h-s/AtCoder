import re

s = input()

pattern = r"A.*Z"

# 部分文字列を集めたリスト
subst_list = re.findall(pattern, s)

# 部分文字列の最大の長さを保持する
max_subst = 0

for s in subst_list:
    if len(s) > max_subst:
        max_subst = len(s)
        
print(max_subst)
