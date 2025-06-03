abc_list = list(map(int, input().split()))

if abc_list[0] == abc_list[1] == abc_list[2]:
    print("Yes")
elif max(abc_list) == sum(abc_list) - max(abc_list):
    print("Yes")
else:
    print("No")
