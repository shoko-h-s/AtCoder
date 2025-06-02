n = int(input())
a_list = list(map(int, input().split()))
q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]

for qu in queries:
    k = qu[1]

    if qu[0] == 1:
        a_list[k-1] = qu[2]

    else:
        print(a_list[k-1])
