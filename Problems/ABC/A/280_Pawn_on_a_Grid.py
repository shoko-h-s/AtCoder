h, w = map(int, input().split())
s_list = [input() for _ in range(h)]

count = 0

for s in s_list:
    count += s.count("#")
    
print(count)
