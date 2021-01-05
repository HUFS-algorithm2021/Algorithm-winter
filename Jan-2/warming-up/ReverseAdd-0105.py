# 백준 1357 임나경
import sys
x, y = map(int, sys.stdin.readline().split())
x = int(str(x)[::-1])
y = int(str(y)[::-1])
print(str(x + y)[::-1])