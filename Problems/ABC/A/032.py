a = int(input())
b = int(input())
n = int(input())

i = n

while (i % a != 0) or (i % b != 0):
    i += 1
    
print(i)
