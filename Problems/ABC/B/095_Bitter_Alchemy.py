n, x = map(int, input().split())
m_list = [int(input()) for _ in range(n)]

# 全種類1種類作った後のお菓子の素
x -= sum(m_list)

count = n

# 全て最小値で作るのが最大量となる
a = x // min(m_list)
count += a

print(count)
