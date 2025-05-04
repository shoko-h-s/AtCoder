n, l = map(int, input().split())
s_list = [input() for _ in range(n)]

# s を辞書順に並べ、結合したものが答え
s_sorted = sorted(s_list)

print("".join(s_sorted))
