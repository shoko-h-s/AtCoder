import collections

n, k = map(int, input().split())
a_list = list(map(int, input().split()))

queue = collections.deque(a_list)

for i in range(k):
    queue.popleft()
    queue.append(0)
    
print(*queue)
