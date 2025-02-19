n = int(input())

# 順不同で良いので、set型を用いる
a_set = set(map(int, input().split()))

# 偶数のみの集合を先に作っておく
a2_set = {a for a in a_set if a % 2 == 0}
enter_flag = True

for a in a2_set:
    if (a % 3 != 0) and (a % 5 != 0):
        enter_flag = False
        print("DENIED")
        break
        
if enter_flag:
    print("APPROVED")
