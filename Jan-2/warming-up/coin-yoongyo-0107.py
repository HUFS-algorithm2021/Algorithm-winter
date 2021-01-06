#백준 11047번 yoongyo

n,k = map(int,input().split())
m = []
cnt = 0

for i in range(n):
    m.append(int(input()))

for i in range(n-1,-1,-1):
    if k == 0:
        break
    elif m[i] > k:
        continue
    cnt += k // m[i]
    k %= m[i]

print(cnt)

