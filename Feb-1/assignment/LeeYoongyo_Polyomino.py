#BOJ 1343 폴리오미노 (이윤교)

import sys
input = sys.stdin.readline
board = input() # 보드판입력

board = board.replace('XXXX','AAAA')
board = board.replace('XX','BB')

if 'X' in board:
    print(-1)
else:
    print(board)
    
