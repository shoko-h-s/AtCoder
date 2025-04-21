x, y = map(int, input().split())

list_1 = [1, 3, 5, 7, 8, 10, 12]
list_2 = [4, 6, 9, 11]

if (x in list_1) and (y in list_1):
    print("Yes")
elif (x in list_2) and (y in list_2):
    print("Yes")
else:
    print("No")
