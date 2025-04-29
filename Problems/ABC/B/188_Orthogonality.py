n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

ab_dot = 0

for a, b in zip(a_list, b_list):
    ab_dot += a * b
    
if ab_dot == 0:
    print("Yes")
else:
    print("No")
