s = [input() for _ in range(12)]

cnt = 0

for i in range(12):
    if len(s[i]) == i+1:
        cnt += 1

print(cnt)
