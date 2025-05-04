n, a, b = map(int, input().split())

# 1回あたりに並べるボールの数
turn = a + b

# 試行回数-1 までを計算する
times = n // turn
balls = a * times

# 最後の試行は余りで場合分け
if n % turn == 0:
    print(balls)
    
else:
    mod = n % turn
    
    # 余りと a、小さい方の値を足す
    print(balls + min(a, mod))
