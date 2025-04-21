n = int(input())
s = input()

if s.count("T") > s.count("A"):
    print("T")
    
elif s.count("T") < s.count("A"):
    print("A")
    
else:
    t_count = 0
    a_count = 0
    win_count = n // 2
    i = 0
    
    while (t_count < win_count) and (a_count < win_count):
        if s[i] == "T":
            t_count += 1
        else:
            a_count += 1
            
        i += 1
            
    if t_count > a_count:
        print("T")
    else:
        print("A")
