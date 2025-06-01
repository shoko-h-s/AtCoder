n = int(input())
p_list = list(map(int, input().split()))

cnt = 0

for i in range(n-2):
    p1, p2, p3 = p_list[i], p_list[i+1], p_list[i+2]

    if (p2 != max(p1, p2, p3)) and (p2 != min(p1, p2, p3)):
        cnt += 1

print(cnt)
