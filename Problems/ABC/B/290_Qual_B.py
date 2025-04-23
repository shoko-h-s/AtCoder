n, k = map(int, input().split())
s = input()

# 予選通過者の人数を記録
passed = 0

result = ""

for i in range(n):
    if (s[i] == "o") and (passed < k):
        result += "o"
        passed += 1
    else:
        result += "x"
    
print(result)
