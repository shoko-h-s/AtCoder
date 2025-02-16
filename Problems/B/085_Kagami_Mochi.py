n = int(input())
d_list = [int(input()) for _ in range(n)]

bucket = [0] * 100

for d in d_list:
    bucket[d-1] += 1
    
print(100 - bucket.count(0))
