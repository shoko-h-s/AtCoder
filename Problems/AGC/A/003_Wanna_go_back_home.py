s = input()
flag = True

# 方角の対応関係が成り立っていない場合は False
if (s.count("N") > 0) and (s.count("S") == 0):
    flag = False
    
if (s.count("S") > 0) and (s.count("N") == 0):
    flag = False
    
if (s.count("W") > 0) and (s.count("E") == 0):
    flag = False
    
if (s.count("E") > 0) and (s.count("W") == 0):
    flag = False
    
if flag:
    print("Yes")
else:
    print("No")
