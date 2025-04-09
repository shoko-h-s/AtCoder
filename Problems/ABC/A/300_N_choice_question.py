n, a, b = map(int, input().split())
c_list = list(map(int, input().split()))

answer = a + b

print(c_list.index(answer) + 1)
