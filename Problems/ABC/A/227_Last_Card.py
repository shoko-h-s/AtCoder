n, k, a = map(int, input().split())

# 次に配る人を格納
person = a

# 順番を次に回す操作を、k-1 回繰り返す
for _ in range(k-1):
    if person == n:
        person = 1
    else:
        person += 1
        
print(person)
