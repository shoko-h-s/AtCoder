s_list = input().split("+")

count = 0

for s in s_list:
    if "0" not in s:
        count += 1
        
print(count)
