a, b = map(int, input().split())

start_time = a + b

if start_time >= 24:
    print(start_time - 24)
else:
    print(start_time)
