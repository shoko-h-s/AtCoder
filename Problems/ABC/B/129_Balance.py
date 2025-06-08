n = int(input())
w_list = list(map(int,input().split()))

min_s1s2 = 10**9

for i in range(1, n):
    s1 = sum(w_list[:i])
    s2 = sum(w_list[i:])
    d = abs(s1 - s2)
    min_s1s2 = min(min_s1s2, d)

print(min_s1s2)
