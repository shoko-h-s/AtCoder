l, r = map(int, input().split())
s = input()

s_slice = s[l-1:r]
s_rev = s_slice[::-1]

print(s[:l-1] + s_rev + s[r:])
