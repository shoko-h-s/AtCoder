x1, x2 = input().split(".")

if x2 == "000":
    print(x1)
elif x2[-2:] == "00":
    print(f"{x1}.{x2[0]}")
elif x2[-1] == "0":
    print(f"{x1}.{x2[:2]}")
else:
    print(f"{x1}.{x2}")
