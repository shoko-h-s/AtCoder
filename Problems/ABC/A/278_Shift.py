n, k = map(int, input().split())
a_list = list(map(int, input().split()))

for i in range(k):
    a_list = a_list[1:]
    a_list.append(0)
    
print(*a_list)
