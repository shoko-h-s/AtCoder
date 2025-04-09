a, b = map(int, input().split())

# a と b が一致しない時のみ、特定可能
if a != b:
    
    # 1 + 2 + 3 = 6 となることを利用
    print(6 - a - b)
    
else:
    print(-1)
