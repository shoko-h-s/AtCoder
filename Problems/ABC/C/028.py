import itertools

abcde_list = list(map(int, input().split()))

xyz_set = set()

for x, y, z in itertools.combinations(abcde_list, 3):
    xyz_set.add(x + y + z)
    
xyz_list = list(xyz_set)
xyz_sorted = sorted(xyz_list, reverse=True)

print(xyz_sorted[2])
