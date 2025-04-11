s = list(input())

while True:
    s.pop()
    
    # s の長さが偶数の場合のみ判定する
    if len(s) % 2 == 0:
        n = len(s) // 2
        
        if s[:n] == s[n:]:
            print(len(s))
            break
