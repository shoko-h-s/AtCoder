a, b = map(int, input().split())
ab_set = {a, b}

num_set = {1, 2, 3}

answer_set = num_set - ab_set

if len(answer_set) == 1:
    print(*answer_set)
else:
    print(-1)
