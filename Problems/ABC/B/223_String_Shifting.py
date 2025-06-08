s = input()

s_min = s
s_max = s

# どちらか片方向のシフトのみでよい
s_left = s

for i in range(len(s)):
    s_left = s_left[1:] + s_left[0]
    s_min = min(s_min, s_left)
    s_max = max(s_max, s_left)

print(s_min)
print(s_max)
