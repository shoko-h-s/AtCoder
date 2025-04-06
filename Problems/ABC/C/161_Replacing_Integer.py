n, k = map(int, input().split())

count = 0
flag = False

# n が k で割り切れる場合、答えは0
if n % k == 0:
    print(0)
    
else:
    n = n % k
    
    # 割り切れない場合は、n % k の値と、そこから1回操作した値の小さい方が答え
    print(min(n, abs(n-k)))
