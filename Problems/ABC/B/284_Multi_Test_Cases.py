t = int(input())

for _ in range(t):
    n = int(input())
    a_list = list(map(int, input().split()))
    
    b_list = [a for a in a_list if a % 2 == 1]
    print(len(b_list))
