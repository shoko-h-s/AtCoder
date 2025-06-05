n = int(input())
a = list(map(int, input().split()))

ans = [a[0]]

for i in range(len(a)-1):
    if i > 0:
        ans.append(a[i])

    if (a[i] < a[i+1]) and (abs(a[i]-a[i+1]) > 1):
        for j in range(a[i]+1, a[i+1]):
            ans.append(j)
    elif (a[i] > a[i+1]) and (abs(a[i]-a[i+1]) > 1):
        for j in range(a[i]-1, a[i+1], -1):
            ans.append(j)

ans.append(a[-1])

print(*ans)
