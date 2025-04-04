import itertools

a_list = list(map(int, input().split()))

# タスク順のリストを生成
task_list = list(itertools.permutations(a_list))
min_cost = 300

# 順番を全探索する
for t in task_list:
    cost = abs(t[1] - t[0]) + abs(t[2] - t[1])
    
    min_cost = min(cost, min_cost)
    
print(min_cost)
