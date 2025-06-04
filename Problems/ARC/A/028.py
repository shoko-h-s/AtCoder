n, a, b = map(int, input().split())

flag_ant = False

while n > 0:
    if n >= a:
        n -= a
    else:
        n = 0

    if n == 0:
        flag_ant = True
        break

    if n >= b:
        n -= b
    else:
        n = 0

if flag_ant:
    print("Ant")
else:
    print("Bug")
