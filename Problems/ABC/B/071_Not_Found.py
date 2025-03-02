s = input()

bucket = [0] * 26

for i in range(len(s)):
    
    # アルファベット小文字の何文字目かを求める（インデックスにしたいので-1）
    c = ord(s[i]) - 97
    
    bucket[c] += 1
    
# カウントが0となる、最も早いインデックスを求める
if bucket.count(0) == 0:
    print("None")
    
else:
    num = bucket.index(0)
    print(chr(num + 97))



# 【備考】
# Training Easy 35
