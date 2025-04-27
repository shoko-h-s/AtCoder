a, b = map(int, input().split())

num_set = {1, 2, 3}

num_set.discard(a)
num_set.discard(b)

if len(num_set) == 1:
    print(*num_set)
else:
    print(-1)
