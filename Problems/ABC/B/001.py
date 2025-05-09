m = int(input())

km = m // 1000

if m < 100:
    vv = "00"

elif 100 <= m <= 5000:
    vv = str(m // 100)

    if len(vv) == 1:
        vv = "0" + vv

elif 6000 <= m <= 30000:
    vv = str(km + 50)

elif 35000 <= m <= 70000:
    vv = str(((km - 30) // 5) + 80)

else:
    vv = "89"

print(vv)
