list_1 = [int(input()) for _ in range(3)]
list_sorted = sorted(list_1, reverse=True)

print(list_sorted.index(list_1[0]) + 1)
print(list_sorted.index(list_1[1]) + 1)
print(list_sorted.index(list_1[2]) + 1)
