a_list = []

# EOF を検出するまで、ループを続ける
while True:
    try:
        a = int(input())
        a_list.append(a)
        
    except:
        break
        
a_reversed = a_list[::-1]

for a in a_reversed:
    print(a)
