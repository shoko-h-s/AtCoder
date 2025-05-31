n = int(input())
xy_list = [list(map(int, input().split())) for _ in range(n)]

t_score = 0
a_score = 0

for xy in xy_list:
    t_score += xy[0]
    a_score += xy[1]

if t_score > a_score:
    print("Takahashi")
elif t_score < a_score:
    print("Aoki")
else:
    print("Draw")
