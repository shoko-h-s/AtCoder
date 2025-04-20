n = int(input())

str = ""

for i in range(1, n+1):
    if i % 3 == 0:
        str += "x"
    else:
        str += "o"
        
print(str)
