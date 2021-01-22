#BOJ 1074번 Z yoongyo

import math
n,r,c = map(int,input().split())
location = 0 #기본 2x2배열에서의 2사분면 / 시작점 (왼쪽 위)

while n > 0:
    if n == 1: #기본 2x2배열로 위치파악(사분면)
        if r == 0 and c == 1: #1사분면 (오른쪽 위)
            location += 1
        elif r == 1 and c == 0: #3사분면 (왼쪽 아래)
            location += 2
        elif r == 1 and c == 1: #4사분면 (오른쪽 아래)
            location += 3

    elif n > 1: #배열의 크기를 2^(n-1) x 2^(n-1)로 4등분으로 쪼개기
        tmp = pow(2, n - 1)
        #찾고자하는 r과 c가 포함된 사분면 찾기 , 왼쪽 위 박스는 그대로
        if tmp > r and tmp <= c: #오른쪽 위
            location += pow(tmp,2) * 1
            c -= tmp
        elif tmp <= r and tmp > c: #왼쪽 아래
            location += pow(tmp,2) * 2
            r -= tmp
        elif tmp <= r and tmp <= c: #오른쪽 아래
            location += pow(tmp,2) * 3
            r -= tmp
            c -= tmp
    n -= 1
print(location)



