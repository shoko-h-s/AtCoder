n = input()

digit_sum = sum(map(int, n))

if digit_sum % 9 == 0:
    print("Yes")
else:
    print("No")
