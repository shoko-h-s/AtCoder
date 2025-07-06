n, q = map(int, input().split())
la_list = [list(map(int, input().split())) for _ in range(n)]
st_list = [list(map(int, input().split())) for _ in range(q)]

for st in st_list:
    print(la_list[st[0]-1][st[1]])
