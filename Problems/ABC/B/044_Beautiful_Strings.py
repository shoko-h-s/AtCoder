import collections

w = input()
count_list = collections.Counter(w)

value_list = list(count_list.values())
value_list_2 = [v for v in value_list if v % 2 == 0]

if len(value_list) == len(value_list_2):
    print("Yes")
else:
    print("No")
