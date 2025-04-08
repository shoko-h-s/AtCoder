a, b = map(int, input().split())

# どちらも正なら負
if a > 0:
    print("Positive")

# 1つ以上が0、またはa, b間に0を含む場合は 0
elif (a == 0) or (b == 0):
    print("Zero")
    
elif (a < 0) and (b > 0):
    print("Zero")
    
# どちらも負なら、整数が奇数個なら負、偶数個なら正
else:
    num = b - a + 1
    
    if num % 2 == 0:
        print("Positive")
        
    else:
        print("Negative")



# 【備考】
# AGC_002
