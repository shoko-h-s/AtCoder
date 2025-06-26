import collections

n = int(input())
s_list = [input() for _ in range(n)]
count_list = collections.Counter(s_list)

print(count_list.most_common()[0][0])
