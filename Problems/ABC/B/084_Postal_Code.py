a, b = map(int, input().split())
s = input()

if s.count("-") != 1:
    print("No")
    
else:
    s_a, s_b = s.split("-")
    
    if (len(s_a) == a) and (len(s_b) == b):
        print("Yes")
        
    else:
        print("No")
