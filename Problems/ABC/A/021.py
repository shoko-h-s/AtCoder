n = int(input())

answer_list = []

while n > 0:
    if n >= 8:
        num = 8
    elif n >= 4:
        num = 4
    elif n >= 2:
        num = 2
    else:
        num = 1

    answer_list.append(num)
    n -= num

answer_list.sort()

print(len(answer_list))

for ans in answer_list:
    print(ans)
