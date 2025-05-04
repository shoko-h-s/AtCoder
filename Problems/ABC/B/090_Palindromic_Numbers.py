a, b = map(int, input().split())

count = 0

for i in range(a, b+1):
    i = str(i)

    i_rev = i[::-1]

    if i == i_rev:
        count += 1

print(count)
