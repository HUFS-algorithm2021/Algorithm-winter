# 백준 15649 임나경

def sequence(a): # 수열
    if a == m:
        for i in range(m):
            print(res[i], end=' ') # 결과 출력
        print()

    for i in range(1, n+1):
        if visit[i] == False: # 방문 안했으면
            visit[i] = True # 방문 후 체크
            res[a] = i # i 대입
            sequence(a + 1) # 재귀호출  a+1
            visit[i] = False # 기초

n, m = map(int, input().split()) # 자연수 1 <= m <= n <= 8
res = [0] * (n+1) # result
visit = [False] * (n+1) # 방문 true, 미방문 false
sequence(0) # 수열 함수 호출
