a, b, c, d = map(int, input().split())

# 2人がそれぞれスイッチを押していた時間のリスト
a_switch = [1 if a <= i <= b else 0 for i in range(101)]
b_switch = [1 if c <= i <= d else 0 for i in range(101)]

ab_switch = [a_switch[i] + b_switch[i] for i in range(101)]

# 値が2となる（2人ともスイッチを押している）インデックスのリストを作成
ab_index = [i for i, x in enumerate(ab_switch) if x == 2]

if len(ab_index) > 0:
# 値が2となる最後のインデックスから、最初のインデックスを引くと答え
    print(ab_index[-1] - ab_index[0])

else:
    print(0)
