a, b = map(int, input().split())

milk_solids = a + b

if (milk_solids >= 15) and (b >= 8):
    print(1)
elif (milk_solids >= 10) and (b >= 3):
    print(2)
elif milk_solids >= 3:
    print(3)
else:
    print(4)
