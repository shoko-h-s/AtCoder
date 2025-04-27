n, x = map(int, input().split())
a_list = list(map(int, input().split()))

check_set = {x}
next_friend = x-1

while True:
    f = a_list[next_friend]
    
    if f not in check_set:
        check_set.add(f)
        next_friend = f-1
        
    else:
        break
        
print(len(check_set))
