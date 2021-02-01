#BOJ 2675번 문자열반복 (이윤교)

import sys
input = sys.stdin.readline
t = int(input())
p=[]
for _ in range(t): #테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)
    r , string = input().split() #반복 횟수 r(1 ≤ r ≤ 8), 문자열 string, 공백 기준으로 입력값 분리
    t = '' #출력문자 t
    for _ in string:
        t += int(r)*_ #반복횟수r과 문자열string을 곱한 후 출력문자에 추가
    print(t)