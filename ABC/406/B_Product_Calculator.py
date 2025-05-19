n, k = map(int, input().split())
list_a = list(map(int, input().split()))

display = 1

for a in list_a:
    display *= a

    if len(str(display)) > k:
        display = 1

print(display)
