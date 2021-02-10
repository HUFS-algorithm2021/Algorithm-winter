# 백준 1343 임나경
import sys

board = sys.stdin.readline().rstrip("\n") # 입력

for i in board:
    if 'XXXX' in board:
        board = board.replace('XXXX', 'AAAA')
    elif 'XX' in board:
        board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)