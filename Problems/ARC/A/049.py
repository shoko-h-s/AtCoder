s = input()
a, b, c, d = map(int, input().split())

# " を文字として扱うため、' で囲む
str = s[:a] + '"' + s[a:]
str = str[:b+1] + '"' + str[b+1:]
str = str[:c+2] + '"' + str[c+2:]
str = str[:d+3] + '"' + str[d+3:]

print(str)
