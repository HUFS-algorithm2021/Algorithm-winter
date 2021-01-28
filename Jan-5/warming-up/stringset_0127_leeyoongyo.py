#BOJ 14425번 문자열 집합 (이윤교)

n,m = map(int,input().split())
string = [] #문자열 n개가 들어있는 리스트
check = [] #검사해야 하는 문자열 m개가 들어있는 리스트
cnt = 0 #포함하는 횟수
for i in range(n):
    string.append(input())
for i in range(m):
    check.append(input())
    if check[i] in string: #입력받은 검사해야 하는 문자열이 집합S에 포함되어있다면
        cnt += 1 #횟수 +1
print(cnt)