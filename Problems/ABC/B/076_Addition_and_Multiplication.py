n = int(input())
k = int(input())

board = 1

for _ in range(n):
    board = min(board*2, board+k)
    
print(board)
