s = input()
ac_flag = True

if s[0] != "A":
    print("WA")
    ac_flag = False
    
elif s[2:len(s)-1].count("C") != 1:
    print("WA")
    ac_flag = False
    
else:
    s = s.replace("A", "")
    s = s.replace("C", "")
    
    if not s.islower():
        print("WA")
        ac_flag = False
        
if ac_flag:
    print("AC")
