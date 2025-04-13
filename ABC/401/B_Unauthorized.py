n = int(input())
s_list = [input() for _ in range(n)]

errors = 0

# ログアウト：0、ログイン：1
log = 0

# publicは必要な操作なし
for s in s_list:
    if (s =="login") and (log == 0):
        log = 1
            
    elif (s == "logout") and (log == 1):
        log = 0
        
    elif (s == "private") and (log == 0):
        errors += 1
        
print(errors)
