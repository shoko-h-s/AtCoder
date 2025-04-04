n = int(input())

s_list = []
p_list = []
flag = False

for _ in range(n):
    s, p = input().split()
    s_list.append(s)
    p_list.append(int(p))
    
# 総人口を求める
peoples = sum(p_list)
    
for i in range(n):
    if p_list[i] > peoples // 2:
        print(s_list[i])
        flag = True
        break
        
if not flag:
    print("atcoder")
