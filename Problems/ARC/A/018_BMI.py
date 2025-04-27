height, bmi = map(float, input().split())

height_m = height / 100

print(bmi * (height_m ** 2))
