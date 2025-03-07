h, w = map(int, input().split())
a_list = [input() for _ in range(h)]

print("#" * (w + 2))

for i in range(h):
    print("#" + a_list[i] + "#")

print("#" * (w + 2))



# 【備考】
# Training Easy 49
