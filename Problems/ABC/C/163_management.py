n = int(input())
a_list = list(map(int, input().split()))

count_list = [0 for _ in range(n)]

for a in a_list:
    count_list[a-1] += 1
    
for c in count_list:
    print(c)
