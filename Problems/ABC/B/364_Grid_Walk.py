h, w = map(int, input().split())
si, sj = map(int, input().split())
c_list = [input() for _ in range(h)]
x = input()

si -= 1
sj -= 1

for i in range(len(x)):
    if (x[i] == "L") and (sj > 0):
        if c_list[si][sj-1] == ".":
            sj -= 1
    elif (x[i] == "R") and (sj < w-1):
        if c_list[si][sj+1] == ".":
            sj += 1
    elif (x[i] == "U") and (si > 0):
        if c_list[si-1][sj] == ".":
            si -= 1
    elif (x[i] == "D") and (si < h-1):
        if c_list[si+1][sj] == ".":
            si += 1

print(si+1, sj+1)
