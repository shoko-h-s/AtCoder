n = int(input())
st_list = [list(input().split()) for _ in range(n)]

st_dict = {}

for st in st_list:
    st_dict[st[0]] = int(st[1])

# dict の値で、降順ソートする
st_sorted = sorted(st_dict.items(), key=lambda x:x[1], reverse=True)

print(st_sorted[1][0])
