# 백준 15650 N과 M (2) (이윤교)

def bt(ind, n, m):
    if ind == m:
        for i in range(m):
            print(m_list[i], end=' ')
        print()
        return
    for i in range(1, n+1):
        if n_list[i] == 1:
            continue
        m_list[ind] = i
        for j in range(i+1):
            n_list[j] = 1
        bt(ind+1, n, m)
        for j in range(1, n+1):
            n_list[j] = 0


n, m = map(int, input().split())  # n까지 m개
n_list = [0 for i in range(n+1)]
m_list = [0 for i in range(m)]

bt(0, n, m)
