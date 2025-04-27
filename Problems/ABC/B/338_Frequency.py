def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]

s = input()

s_dict = {}

for i in range(len(s)):
    if s[i] in s_dict:
        s_dict[s[i]] += 1
    else:
        s_dict[s[i]] = 1
        
s_max = max(s_dict.values())
keys = get_keys_from_value(s_dict, s_max)

keys_sorted = sorted(keys)

print(keys_sorted[0])
