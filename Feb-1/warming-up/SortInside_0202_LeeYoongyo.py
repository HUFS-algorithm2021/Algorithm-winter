#BOJ 1427 소트인사이드 (이윤교)
import sys
input = sys.stdin.readline
n = list(map(str,input()))
L = []
for i in n:
    L.append(i)
result = sorted(L,reverse=True)
print(''.join(result))