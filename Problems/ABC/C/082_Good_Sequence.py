import collections

n = int(input())
a_list = list(map(int, input().split()))

c = collections.Counter(a_list)
c_sorted = sorted(c.items())

count = 0

for c in c_sorted:
    if c[0] > c[1]:
        count += c[1]
    elif c[0] < c[1]:
        count += c[1] - c[0]
        
print(count)
