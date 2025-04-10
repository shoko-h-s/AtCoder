n = int(input())

for i in range(n, 920):
    str_i = str(i)
    
    if int(str_i[0]) * int(str_i[1]) == int(str_i[2]):
        print(i)
        break
