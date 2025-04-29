import collections

n = int(input())
s_list = [input() for _ in range(n)]

c = collections.Counter(s_list)

print(c.most_common()[0][0])
