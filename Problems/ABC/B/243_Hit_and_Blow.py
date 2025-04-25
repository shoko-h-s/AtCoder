n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

count = 0

for i in range(n):
    if a_list[i] == b_list[i]:
        count += 1
        
print(count)

a_set = set(a_list)
b_set = set(b_list)
ab_set = a_set & b_set

print(len(ab_set) - count)
