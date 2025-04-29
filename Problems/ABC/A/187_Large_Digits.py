a, b = input().split()

if sum(map(int, a)) >= sum(map(int, b)):
    print(sum(map(int, a)))
else:
    print(sum(map(int, b)))
