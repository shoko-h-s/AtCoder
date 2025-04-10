n = int(input())

mod_n = n % 5

if mod_n == 0:
    print(n)
elif mod_n <= 2:
    print(n - mod_n)
else:
    print(n + (5 - mod_n))
