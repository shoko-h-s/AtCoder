n = int(input())
w_list = list(input().split())

# 最後の単語から . を取り除く必要あり
w_list[-1] = w_list[-1].replace(".", "")

print(w_list.count("TAKAHASHIKUN") + w_list.count("Takahashikun") + w_list.count("takahashikun"))
