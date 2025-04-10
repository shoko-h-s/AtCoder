n = int(input())
w_list = list(input().split())

words = ["and", "not", "that", "the", "you"]
flag = False

for w in w_list:
    if w in words:
        flag = True
        break
        
if flag:
    print("Yes")
else:
    print("No")
