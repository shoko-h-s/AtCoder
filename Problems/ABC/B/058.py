o = input()
e = input()

password = ""

if len(o) == len(e):
    for i in range(len(o)):
        password += o[i] + e[i]
        
else:
    for i in range(len(e)):
        password += o[i] + e[i]
        
    password += o[-1]
    
print(password)
