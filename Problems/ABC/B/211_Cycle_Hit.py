s_list = [input() for _ in range(4)]

count_list = [0, 0, 0, 0]

for s in s_list:
    if s == "H":
        count_list[0] += 1
    elif s == "2B":
        count_list[1] += 1
    elif s == "3B":
        count_list[2] += 1
    else:
        count_list[3] += 1
        
if count_list[0] == count_list[1] == count_list[2] == count_list[3]:
    print("Yes")
else:
    print("No")
