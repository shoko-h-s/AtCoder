n, t = map(int, input().split())
c_list = list(map(int, input().split()))
r_list = list(map(int, input().split()))

if t in c_list:
    color = t
else:
    color = c_list[0]

max_c = 0
winner = 0

for i in range(n):
    if c_list[i] == color:
        if max_c < r_list[i]:
            max_c = r_list[i]
            winner = i + 1

print(winner)
