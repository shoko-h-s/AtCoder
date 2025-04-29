n, l = map(int, input().split())
a_list = list(map(int, input().split()))

al_list = [a for a in a_list if a >= l]

print(len(al_list))
