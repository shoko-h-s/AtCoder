s_list = [input() for _ in range(12)]

sr_list = [s for s in s_list if "r" in s]

print(len(sr_list))
