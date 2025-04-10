n = int(input())
a_list = list(map(int, input().split()))

for i in range(2001):
    if i not in a_list:
        print(i)
        break
