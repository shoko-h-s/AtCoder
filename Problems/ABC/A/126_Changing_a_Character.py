n, k = map(int, input().split())
s = input()


if k == 1:
    print(s[0].lower() + s[1:])
    
else:
    s1 = s[:k-1]
    s2 = s[k:]

    c_lower = s[k-1].lower()

    print(s1 + c_lower + s2)
