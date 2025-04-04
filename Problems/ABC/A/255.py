r, c = map(int, input().split())
a_list = [list(map(int, input().split())) for i in range(2)]

print(a_list[r-1][c-1])
