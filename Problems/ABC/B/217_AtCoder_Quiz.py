contest_set = {"ABC", "ARC", "AGC", "AHC"}

s_set = {input() for _ in range(3)}

answer_set = contest_set - s_set

print(*answer_set)
