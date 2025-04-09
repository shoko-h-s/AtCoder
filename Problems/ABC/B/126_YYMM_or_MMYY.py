s = input()

yymm = int(s[2:])
mmyy = int(s[:2])

if (1 <= yymm <= 12) and (1 <= mmyy <= 12):
    print("AMBIGUOUS")
elif 1 <= yymm <= 12:
    print("YYMM")
elif 1 <= mmyy <= 12:
    print("MMYY")
else:
    print("NA")
