num_set = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

s_list = list(input())
s_set = set(s_list)

answer_set = num_set - s_set

print(*answer_set)
