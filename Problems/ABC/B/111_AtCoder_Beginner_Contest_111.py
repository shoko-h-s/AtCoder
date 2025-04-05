import math

n = int(input())

if n <= 111:
    print(111)
else:
    print(111 * math.ceil(n / 111))
