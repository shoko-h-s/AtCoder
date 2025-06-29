n = int(input())
a_list = [input() for _ in range(n)]

flag = True

for i in range(n):
    for j in range(i+1, n):
        if (a_list[i][j] == "W") and (a_list[j][i] != "L"):
            flag = False
            break

        elif (a_list[i][j] == "L") and (a_list[j][i] != "W"):
            flag = False
            break

        elif (a_list[i][j] == "D") and (a_list[j][i] != "D"):
            flag = False
            break

if flag:
    print("correct")
else:
    print("incorrect")
