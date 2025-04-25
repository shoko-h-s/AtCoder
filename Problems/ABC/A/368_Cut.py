n, k = map(int, input().split())
a_list = list(map(int, input().split()))

under_cards = a_list[-k:]
up_cards = a_list[:-k]
new_list = under_cards + up_cards

print(*new_list)
