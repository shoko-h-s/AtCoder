s = input()

flag = False

if s[0] == "A":
    if s[2:-1].count("C") == 1:
        s = s.replace("A", "")
        s = s.replace("C", "")

        if s.islower():
            flag = True

if flag:
    print("AC")
else:
    print("WA")
