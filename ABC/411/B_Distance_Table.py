n = int(input())
d_list = list(map(int, input().split()))

for i in range(n-1):
    line = []
    d = d_list[i]
    line.append(d)

    for j in range(i+1, n-1):
        d += d_list[j]
        line.append(d)

    print(*line)
