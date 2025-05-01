import re

s = input()

if re.fullmatch("[A-Za-z]*[I|i][A-Za-z]*[C|c][A-Za-z]*[T|t][A-Za-z]*", s):
    print("YES")
else:
    print("NO")
