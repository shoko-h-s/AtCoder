import numpy as np

n, m, c = map(int, input().split())
b_list = list(map(int, input().split()))
a_list = [list(map(int, input().split())) for _ in range(n)]

b_np = np.array(b_list)
a_np = np.array(a_list)

count = 0

for a in a_np:
    # 各ソースコードと b_list の内積を求める
    if np.dot(a, b_np) + c > 0:
        count += 1
        
print(count)



# 【備考】
# Training Easy 5
