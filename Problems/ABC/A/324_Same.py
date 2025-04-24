n = int(input())
a_list = list(map(int, input().split()))

a_set = set(a_list)

if len(a_set) == 1:
    print("Yes")
else:
    print("No")
