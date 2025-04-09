n, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

score = 0

for b in b_list:
    score += a_list[b-1]
    
print(score)
