# 백준 15650 강다인

from itertools import combinations # 조합 라이브러리

N, M = map(int, input().split())

for i in combinations(range(1, N+1), M): # 1부터 n까지 중 m개를 뽑는 조합, 오름차순
    print(' '.join(list(map(str, i))))