n = int(input())
xy_list = [input() for _ in range(n)]

t_score = 0
a_score = 0

for xy in xy_list:
    x, y = map(int, xy.split())    
    t_score += x
    a_score += y
    
if t_score > a_score:
    print("Takahashi")
elif t_score < a_score:
    print("Aoki")
else:
    print("Draw")
