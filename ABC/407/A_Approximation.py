a, b = map(int, input().split())

num_real = a / b

num_1 = a // b
num_2 = (a + b - 1) // b

if abs(num_real - num_1) < abs(num_real - num_2):
    print(num_1)
else:
    print(num_2)
