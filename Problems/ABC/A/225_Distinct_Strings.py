s = input()

s_set = set(s)

if len(s_set) == 1:
    print(1)
elif len(s_set) == 2:
    print(3)
else:
    print(6)
