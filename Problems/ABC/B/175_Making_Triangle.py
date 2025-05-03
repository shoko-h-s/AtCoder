n = int(input())

l_list = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i < j < k:
                li = l_list[i]
                lj = l_list[j]
                lk = l_list[k]
                set_ijk = {li, lj, lk}

                # 三角形を作る条件：2辺の長さの和は他の1辺の長さより大きい
                if sum(set_ijk) - max(set_ijk) > max(set_ijk):
                    count += 1

print(count)
