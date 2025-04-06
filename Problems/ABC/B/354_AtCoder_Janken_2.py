n = int(input())

s_list = []
total_rate = 0

for _ in range(n):
    s, c = input().split()
    total_rate += int(c)
    s_list.append(s)
    
s_sorted = sorted(s_list)
winner = total_rate % n

print(s_sorted[winner])
