abcde_list = list(map(int, input().split()))

abcde_set = set(abcde_list)
check_list = list(abcde_set)

if (len(check_list) == 2) and ((abcde_list.count(check_list[0]) == 2) or (abcde_list.count(check_list[0]) == 3)):
    print("Yes")
else:
    print("No")
