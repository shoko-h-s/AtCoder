x = input()

x_list = [int(x[i]) for i in range(4)]

weak_flag = False
weak_count = 0

if x_list[0] == x_list[1] == x_list[2] == x_list[3]:
    print("Weak")
    
else:
    for j in range(3):
        if (x_list[j] + 1 == x_list[j+1]) or ((x_list[j] == 9) and (x_list[j+1] == 0)):
            weak_count += 1
            
    if weak_count == 3:
        print("Weak")
    else:
        print("Strong")
