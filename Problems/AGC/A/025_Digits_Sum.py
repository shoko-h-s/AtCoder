n = int(input())

answer = 10**5

for a in range(1, n):
    b = n - a

    ab = sum(map(int, str(a))) + sum(map(int, str(b)))

    answer = min(answer, ab)

print(answer)
