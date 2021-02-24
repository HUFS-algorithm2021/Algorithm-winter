# 백준 15650 임나경
def sequence(a, index): # 수열
    if a == m:
        for i in range(m):
            print(res[i], end=' ') # 결과 출력
        print()

    for i in range(index, n+1):
        if visit[i] == False: # 방문 안했으면
            visit[i] = True # 방문 후 체크
            res[a] = i # i 대입
            sequence(a + 1, i + 1) # 재귀호출  a+1
            visit[i] = False # 초기화

n, m = map(int, input().split()) # 자연수 1 <= m <= n <= 8
res = [0] * (n+1) # result
visit = [False] * (n+1) # 방문 true, 미방문 false
sequence(0, 1) # 수열 함수 호출
