import string

# 英小文字のリストをあらかじめ作っておく
chr_list = list(string.ascii_lowercase)

p_list = list(map(int, input().split()))

str = ""

for p in p_list:
    str += chr_list[p-1]
    
print(str)
