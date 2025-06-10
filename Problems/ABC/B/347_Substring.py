s = input()

word_set = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        word = s[i:j+1]
        word_set.add(word)

print(len(word_set))
