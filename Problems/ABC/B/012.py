n = int(input())

h, ms = divmod(n, 3600)
m, s = divmod(ms, 60)

h = str(h).zfill(2)
m = str(m).zfill(2)
s = str(s).zfill(2)

print(f"{h}:{m}:{s}")
