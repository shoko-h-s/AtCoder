n = input()

n_new = ""

for i in range(3):
    if n[i] == "1":
        n_new += "9"
    else:
        n_new += "1"
        
print(n_new)
