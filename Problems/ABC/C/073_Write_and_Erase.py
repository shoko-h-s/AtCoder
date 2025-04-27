n = int(input())
a_list = [int(input()) for _ in range(n)]

paper_dict = {}

for a in a_list:
    if a in paper_dict:
        paper_dict[a] += 1
    else:
        paper_dict[a] = 1
        
count = 0        

for value in paper_dict.values():
    if value % 2 == 1:
        count += 1
        
print(count)
