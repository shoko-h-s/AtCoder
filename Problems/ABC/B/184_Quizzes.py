n, x = map(int, input().split())
s = list(input())

for i in range(n):
    if s[i] == "o":
        x += 1
    elif x > 0:
        x -= 1
        
print(x)
