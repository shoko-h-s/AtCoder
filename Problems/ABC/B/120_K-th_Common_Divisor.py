a, b, k = map(int, input().split())

# a, b のうち、小さい方までループを回す
times = min(a, b)

list_1 = []

for i in range(1, times + 1):
    if (a % i == 0) and (b % i == 0):
        list_1.append(i)
        
list_1_sorted = sorted(list_1, reverse=True)

print(list_1_sorted[k-1])
