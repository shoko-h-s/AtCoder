n, x = map(int, input().split())

str_1 = ""

for i in range(26):
    str_1 += (chr(65+i)) * n
              
print(str_1[x-1])
