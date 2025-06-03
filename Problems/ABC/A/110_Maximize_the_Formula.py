abc_list = list(map(int, input().split()))

abc_list.sort(reverse=True)

x = int(str(abc_list[0]) + str(abc_list[1]))

print(x + abc_list[2])
