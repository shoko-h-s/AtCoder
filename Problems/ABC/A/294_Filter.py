n = int(input())
a_list = list(map(int, input().split()))

even_list = [a for a in a_list if a % 2 == 0]

print(*even_list)
