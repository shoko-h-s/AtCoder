import collections

n = int(input())
a_list = list(map(int, input().split()))

c = collections.Counter(a_list)
c_values = list(c.values())

count = 0

for v in c_values:
    count += v // 2
    
print(count)
