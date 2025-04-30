import numpy as np

n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_np = np.array(a_list)
b_np = np.array(b_list)

if np.dot(a_np, b_np) == 0:
    print("Yes")
else:
    print("No")
