a, b = map(int, input().split())

# a の値を tmp に格納し、a, b の入れ替えを行う　
tmp = a
a = b
b = tmp

print(a, b)
