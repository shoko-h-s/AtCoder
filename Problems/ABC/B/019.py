import itertools

s = input()

s_groupby = list((key, len(list(group))) for key, group in itertools.groupby(s))

answer = ""

for sg in s_groupby:
    answer += sg[0]
    answer += str(sg[1])
    
print(answer)
