txa, tya, txb, tyb, t, v = map(int, input().split())
n = int(input())
list_xy = [list(map(int, input().split())) for _ in range(n)]

move = t * v
flag = False

for xy in list_xy:
    d_1 = ((xy[0] - txa)**2 + (xy[1] - tya)**2)**0.5
    d_2 = ((txb - xy[0])**2 + (tyb - xy[1])**2)**0.5

    if d_1 + d_2 <= move:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")
