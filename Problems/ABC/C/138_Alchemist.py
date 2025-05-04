n = int(input())
v_list = list(map(int, input().split()))

# 降順にソート
v_sorted = sorted(v_list, reverse=True)

# リストの末尾を操作するようにし、高速化を図る
for _ in range(n-1):
    new_v = (v_sorted[-1] + v_sorted[-2]) / 2
    v_sorted.pop()
    v_sorted.pop()
    v_sorted.append(new_v)
    
print(v_sorted[0])
