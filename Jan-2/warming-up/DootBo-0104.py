# 백준 1764 임나경
import sys
n, m = map(int, sys.stdin.readline().split())
lst1 = [sys.stdin.readline().strip() for _ in range(n)]
lst2 = [sys.stdin.readline().strip() for _ in range(m)]

cnt = list(set(lst1) & set(lst2)) # 듣보잡 리스트
# 두 리스트의 교집합을 구할 때 & 사용

print(len(cnt))
cnt.sort() # cnt 사전순 배열
[print(cnt[_]) for _ in range(len(cnt))]