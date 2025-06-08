n, t, p = map(int, input().split())
l_list = list(map(int, input().split()))

i = 0

while True:
    people = 0

    for l in l_list:
        if l + i >= t:
            people += 1

    if people >= p:
        break

    i += 1

print(i)
