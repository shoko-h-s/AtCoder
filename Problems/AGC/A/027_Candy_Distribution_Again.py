n, x = map(int, input().split())
a_list = list(map(int, input().split()))

a_list.sort()

count = 0

for i in range(n):
    if i == n - 1:
        if a_list[i] == x:
            count += 1

    elif x >= a_list[i]:
        count += 1
        x -= a_list[i]

    else:
        break

print(count)
