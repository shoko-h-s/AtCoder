n = int(input())
str_n = str(n)

if n >= 42:
    str_n = str(n+1)
else:
    str_n = str(n)
    
print("AGC" + str_n.zfill(3))
