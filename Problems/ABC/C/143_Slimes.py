import itertools

n = int(input())
s = input()

s_groupby = list((key, len(list(group))) for key, group in itertools.groupby(s))
    
print(len(s_groupby))
