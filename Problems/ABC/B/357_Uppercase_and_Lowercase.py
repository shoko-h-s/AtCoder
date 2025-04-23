s = input()

# 大文字、小文字をそれぞれカウント
count_list = ["u" if s[i].isupper() else "l" for i in range(len(s))]

if count_list.count("u") > count_list.count("l"):
    print(s.upper())
else:
    print(s.lower())
