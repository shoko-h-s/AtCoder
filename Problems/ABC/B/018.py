s = input()
n = int(input())
lr_list = [input() for _ in range(n)]

for lr in lr_list:
    l, r = map(int, lr.split())
    
    # 部分反転の操作
    s_slice = s[l-1:r]
    s_rev = s_slice[::-1]
    
    s = s[:l-1] + s_rev + s[r:]
    
print(s)
