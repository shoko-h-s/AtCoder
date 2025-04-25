num_set = {1, 2, 3}

ab_set = {int(input()) for _ in range(2)}

answer_set = num_set - ab_set

print(*answer_set)
