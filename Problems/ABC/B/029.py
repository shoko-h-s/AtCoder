s_list = [input() for _ in range(12)]

count = 0

for s in s_list:
    if "r" in s:
        count += 1
        
print(count)
