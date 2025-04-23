k = int(input())

h = "21"

if k >= 60:
    k -= 60
    h = "22"
    
print(h + ":" + str(k).zfill(2))
