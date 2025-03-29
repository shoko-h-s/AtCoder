s1 = input()
s2 = input()
s3 = input()
t = input()

str = ""

for i in range(len(t)):
    if t[i] == "1":
        str += s1
    elif t[i] == "2":
        str += s2
    else:
        str += s3
        
print(str)
