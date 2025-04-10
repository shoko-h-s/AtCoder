n = int(input())
h_list = list(map(int, input().split()))

h_max = max(h_list)

if h_max == h_list[0]:
    print(-1)
else:
    for i in range(1, n):
        if h_list[0] < h_list[i]:
            print(i+1)
            break
