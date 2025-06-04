n = int(input())

if n % 2 == 0:
    len_hypen = (n-2) // 2
    print("-" * len_hypen + "==" + "-" * len_hypen)
else:
    len_hypen = (n-1) // 2
    print("-" * len_hypen + "=" + "-" * len_hypen)
