n = int(input())
s, t = input().split()

string = ""

for i in range(n):
    string += s[i]
    string += t[i]
    
print(string)
