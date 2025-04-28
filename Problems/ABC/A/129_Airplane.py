import itertools

pqr_list = list(map(int, input().split()))

min_time = 300

# 組み合わせを全探索する
for pair in itertools.combinations(pqr_list, 2):
    total_time = sum(pair)
    min_time = min(min_time, total_time)
    
print(min_time)
