n = int(input())
a_list = list(map(int, input().split()))

alice = 0
bob = 0

a_sorted = sorted(a_list, reverse=True)

for i in range(n):
    if i % 2 == 0:
        alice += a_sorted[i]
        
    else:
        bob += a_sorted[i]

print(alice - bob)

