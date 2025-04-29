n = int(input())

digit_sum = sum(map(int, str(n)))

if n % digit_sum == 0:
    print("Yes")
else:
    print("No")
