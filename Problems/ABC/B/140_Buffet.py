n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

ans = 0
before_dish = -1

for a in a_list:
    ans += b_list[a-1]

    if before_dish + 1 == a:
        ans += c_list[a-2]

    before_dish = a

print(ans)
