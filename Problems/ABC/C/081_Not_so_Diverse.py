import collections

n, k = map(int, input().split())
a_list = list(map(int, input().split()))

d = collections.defaultdict(int)

for a in a_list:
    d[a] += 1

d_sorted = sorted(d.items(), key=lambda x:x[1])
d_list = [item[1] for item in d_sorted]
queue = collections.deque(d_list)

count = 0

while len(queue) > k:
    count += queue.popleft()

print(count)
