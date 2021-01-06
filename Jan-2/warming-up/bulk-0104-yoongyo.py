 # 백준 7568번 yoongyo

n = int(input())
A = []
B = []
for i in range (n):
	A.append(input().split())

for i in range (n):
    tmp = 1
    for j in range(n):
        if A[i][0] < A[j][0] and A[i][1]<A[j][1]:
            tmp += 1
    B.append(tmp)

for i in B:
    print(i,end=' ')