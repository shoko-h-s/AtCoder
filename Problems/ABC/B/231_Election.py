# dict の値からキーを取得する関数
def get_key_from_value(d, val):
    keys = [k for k, v in d.items() if v == val]
    
    if keys:
        return keys[0]
    
    return None


n = int(input())
s_list = [input() for _ in range(n)]

s_dict = {}

for s in s_list:
    if s in s_dict:
        s_dict[s] += 1
    else:
        s_dict[s] = 1
        
s_max = max(s_dict.values())
key = get_key_from_value(s_dict, s_max)

print(key)
