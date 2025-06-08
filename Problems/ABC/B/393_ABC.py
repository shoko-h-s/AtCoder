s = input()

cnt = 0

for i in range(len(s)):
    if s[i] == "A":

        for j in range(i+1, len(s)):
            if s[j] == "B":

                for k in range(j+1, len(s)):
                    if (s[k] == "C") and (j-i == k-j):
                        cnt += 1

print(cnt)
