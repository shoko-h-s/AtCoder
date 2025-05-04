n, a, b = map(int, input().split())

answer_list = [i for i in range(1, n+1) if a <= sum(map(int, str(i))) <= b]

print(sum(answer_list))
