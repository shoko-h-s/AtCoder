n = int(input())
s_list = list(input())

answer = 0

for i in range(n-1):
    x_list = s_list[:i+1]
    y_list = s_list[i+1:]
    
    x_set = set(x_list)
    y_set = set(y_list)
    answer_set = x_set & y_set
    
    answer = max(answer, len(answer_set))
    
print(answer)
