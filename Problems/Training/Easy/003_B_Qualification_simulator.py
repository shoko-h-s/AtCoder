n, a, b = map(int, input().split())
s = input()

d_students = 0
o_students = 0

for i in range(n):
    if s[i] == "c":
        print("No")
    
    elif s[i] == "a":
        if d_students + o_students < a + b:
            print("Yes")
            d_students += 1
            
        else:
            print("No")
            
    else:
        if (d_students + o_students < a + b) and (b > o_students):
            print("Yes")
            o_students += 1
            
        else:
            print("No")
