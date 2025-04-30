import itertools

s, k = input().split()
k = int(k)

per_set = set(list(itertools.permutations(s)))
per_sorted = sorted(list(per_set))
per_sorted = ["".join(per) for per in per_sorted]

print(per_sorted[k-1])
