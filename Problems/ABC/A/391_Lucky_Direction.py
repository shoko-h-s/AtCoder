d = input()

d_list = ["N", "E", "W", "S", "NE", "NW", "SE", "SW"]
d2_list = ["S", "W", "E", "N", "SW", "SE", "NW", "NE"]

for i in range(8):
    if d_list[i] == d:
        print(d2_list[i])
        break
