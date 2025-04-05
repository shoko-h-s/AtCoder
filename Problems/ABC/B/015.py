n = int(input())
a_list = list(map(int, input().split()))

a_list = [a for a in a_list if a != 0]
bugs = sum(a_list)
num = len(a_list)

print((bugs + num - 1) // num)
