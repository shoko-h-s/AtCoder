n = int(input())
s_list = [input() for _ in range(n)]

result_dict = {}

for s in s_list:
    if s in result_dict:
        result_dict[s] += 1
    else:
        result_dict[s] = 1
        
max_result = max(result_dict.values())

# 最大値を値に持つキーをリスト化する
keys = [k for k, v in result_dict.items() if v == max_result]
answer_list = sorted(keys)

for a in answer_list:
    print(a)
