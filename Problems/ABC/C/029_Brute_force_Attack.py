import itertools

n = int(input())

for abc in itertools.product(["a", "b", "c"], repeat=n):
    print("".join(abc))
