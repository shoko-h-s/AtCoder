n, k = map(int, input().split())
a_list = list(map(int, input().split()))

cnt = 0
seat = k

for a in a_list:
    if a > seat:
        cnt += 1
        seat = k - a
    else:
        seat -= a

print(cnt + 1)
