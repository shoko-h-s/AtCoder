n, q = map(int, input().split())

buckets = [0] * (n+1)

for _ in range(q):
    event, x = map(int, input().split())

    if event == 1:
        buckets[x] += 1
    elif event == 2:
        buckets[x] = 2
    else:
        if buckets[x] == 2:
            print("Yes")
        else:
            print("No")
