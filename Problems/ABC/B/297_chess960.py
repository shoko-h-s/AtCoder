s = input()

b1 = s.find("B")
b2 = s.rfind("B")

r1 = s.find("R")
r2 = s.rfind("R")
k = s.find("K")

flag = False

# 2 数の偶奇が異なる → 差が奇数となる
if (b2 - b1) % 2 == 1:
    if r1 < k < r2:
        flag = True
        
if flag:
    print("Yes")
else:
    print("No")
