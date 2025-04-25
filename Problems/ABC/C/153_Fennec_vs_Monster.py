n, k = map(int, input().split())
h_list = list(map(int, input().split()))

if n <= k:
    print(0)

else:
    # h_list から、値の大きな順に k 番目までを取り除き、合計を出す
    h_sorted = sorted(h_list, reverse=True)
    new_list = h_sorted[k:]
    
    print(sum(new_list))
