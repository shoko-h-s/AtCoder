n = int(input())
t = input()

# 方向、東南西北
way = 0
x = 0
y = 0

for i in range(n):
    if t[i] == "S":
        if way == 0:
            x += 1
        elif way == 1:
            y -= 1
        elif way == 2:
            x -= 1
        else:
            y += 1

    else:
        if way == 3:
            way = 0
        else:
            way += 1

print(x, y)
