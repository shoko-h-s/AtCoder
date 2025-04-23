n = int(input())
a_list = list(map(int, input().split()))

count = 0

for i in range(len(a_list)-2):
    if a_list[i] == a_list[i+2]:
        count += 1
        
print(count)
