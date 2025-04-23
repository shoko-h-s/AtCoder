s = input()

num_list = [s[i] if s[i].isdigit() else "" for i in range(len(s))]

print("".join(num_list))
