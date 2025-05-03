s = input()

alphabet = list("abcdefghijklmnopqrstuvwxyz")

for i in range(26):
    if alphabet[i] not in s:
        print(alphabet[i])
        break
