a, b = input().split()

s1 = a * int(b)
s2 = b * int(a)

if s1 <= s2:
    print(s1)
else:
    print(s2)
