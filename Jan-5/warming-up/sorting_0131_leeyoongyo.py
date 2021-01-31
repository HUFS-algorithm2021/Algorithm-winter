#BOJ 2750 수 정렬하기 (이윤교)
import sys

input = sys.stdin.readline
n = int(input())
num = sorted(int(input()) for _ in range(n))

for _ in range(n):
    print(num[_])