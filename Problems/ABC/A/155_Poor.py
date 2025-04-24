num_list = list(map(int, input().split()))

num_set = set(num_list)

if len(num_set) == 2:
    print("Yes")
else:
    print("No")
