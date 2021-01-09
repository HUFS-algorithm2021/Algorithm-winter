# 20519 백준 강다인

import sys # input 함수도 시간복잡도에 영향을 준다........................
input = sys.stdin.readline

test = int(input())

while test:
    test -= 1
    person = int(input())
    mbti = list(map(str, input().split()))
    
    minn = 200 # 최대치, 적당한 값으로 잡기
    i=0

    if person > 32: # 비둘기 집 원리. 시간초과 잡는 방법
        print(0)
    else: # 브루트 포스
        for i in range(person):
            for j in range(person):
                for o in range(person):
                    if i == j or i == o or j == o:
                        continue
                    temp = 0
                    for x in range(4):
                        if mbti[i][x] != mbti[j][x]: temp += 1
                        if mbti[j][x] != mbti[o][x]: temp += 1
                        if mbti[i][x] != mbti[o][x]: temp += 1
                    minn = min(minn, temp) # 최소값 갱신
        print(minn)