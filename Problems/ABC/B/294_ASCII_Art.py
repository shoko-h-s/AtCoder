h, w = map(int, input().split())
a_list = [list(map(int, input().split())) for _ in range(h)]

for i in range(h):
    line = ""
    
    for j in range(w):
        if a_list[i][j] == 0:
            line += "."
        else:
            line += chr(a_list[i][j]+64)
            
    print(line)
