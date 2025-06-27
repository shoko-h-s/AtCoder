from collections import defaultdict

n, k = map(int, input().split())

sweets_dict = defaultdict(int)
cnt = 0

for _ in range(k):
    d = int(input())
    a_list = list(map(int, input().split()))

    for a in a_list:
        sweets_dict[a] += 1

# お菓子が 0 個 = dict にキーが存在しない
for i in range(1, n+1):
    if i not in sweets_dict:
        cnt += 1

print(cnt)
