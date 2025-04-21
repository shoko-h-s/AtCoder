n = input()

# 集合を作り、要素数が 1 なら SAME
n_set = set(n)

if len(n_set) == 1:
    print("SAME")
else:
    print("DIFFERENT")
