h, w = map(int, input().split())
r, c = map(int, input().split())

# 一旦、すべての辺で隣接する設定にする
count = 4

# (r, c) が各端となる条件を果たす場合、カウントを減らす
if r == 1:
    count -= 1
    
if c == 1:
    count -= 1
    
if r == h:
    count -= 1
    
if c == w:
    count -= 1
    
print(count)
