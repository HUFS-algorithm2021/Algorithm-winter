# 백준 15649 임나경

def sequence(a):
    if a == m:
        for i in range(m):
            print(res[i], end=' ')
        print()

    for i in range(1, n+1):
        if visit[i] == False:
            visit[i] = True
            res[a] = i
            sequence(a + 1)
            visit[i] = False

n, m = map(int, input().split())
res = [0] * (n+1)
visit = [False] * (n+1)
sequence(0)
