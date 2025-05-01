import re

s = input()

if re.fullmatch("<=+>", s):
    print("Yes")
else:
    print("No")
