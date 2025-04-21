n = int(input())
st_list = [input() for _ in range(n)]

st_set = set(st_list)

if len(st_set) == n:
    print("No")
else:
    print("Yes")
