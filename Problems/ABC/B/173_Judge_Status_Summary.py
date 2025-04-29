import collections

n = int(input())
s_list = [input() for _ in range(n)]

c = collections.Counter(s_list)

ac = c["AC"]
wa = c["WA"]
tle = c["TLE"]
re = c["RE"]

print(f"AC x {ac}")
print(f"WA x {wa}")
print(f"TLE x {tle}")
print(f"RE x {re}")
