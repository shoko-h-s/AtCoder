n = int(input())
key_list = [list(input().split()) for _ in range(n)]

left_flag = False
right_flag = False
left_hand = 0
right_hand = 0
ans = 0

for key in key_list:
    if key[1] == "L":
        if not left_flag:
            left_hand = int(key[0])
            left_flag = True
        else:
            ans += abs(left_hand - int(key[0]))
            left_hand = int(key[0])
    else:
        if not right_flag:
            right_hand = int(key[0])
            right_flag = True
        else:
            ans += abs(right_hand - int(key[0]))
            right_hand = int(key[0])

print(ans)
