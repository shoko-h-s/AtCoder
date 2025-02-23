x = int(input())

def prime_number(x):
    
    # 1以下の整数は、素数ではない
    if x <= 1:
        return False
    
    # 2は素数、それ以外の偶数は素数ではない
    elif x == 2:
        return True
    
    elif x % 2 == 0:
        return False
    
    # 3以降の奇数のみをループで調べれば良い
    else:
        
        # nの平方根をint型に修正する必要あり（小数点以下切り上げ）
        for i in range(3, int(x**0.5)+1, 2):
            if x % i == 0:
                return False
        
        else:
            return True


while True:
    if prime_number(x):
        print(x)
        break
        
    else:
        x += 1

# 【別解】
#　sympyライブラリのisprime()を用いると、もっと簡潔に書けるが遅くなる


# 【備考】
# Training Easy 21
