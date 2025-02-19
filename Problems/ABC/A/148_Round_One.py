a = int(input())
b = int(input())

wa_list = [a, b]

# リストにない要素が答えになる
if wa_list.count(1) == 0:
    print(1)
    
elif wa_list.count(2) == 0:
    print(2)
    
else:
    print(3)
