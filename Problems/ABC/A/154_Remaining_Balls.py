s, t = input().split()
a, b = map(int, input().split())
u = input()

if s == u:
    a -= 1
else:
    b -= 1
    
print(a, b)
