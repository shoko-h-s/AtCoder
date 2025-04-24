q = int(input())
query = [input() for _ in range(q)]

a_list = []

for qu in query:
    num, xk = map(int, qu.split())
    
    if num == 1:
        a_list.append(xk)
    else:
        print(a_list[-xk])
