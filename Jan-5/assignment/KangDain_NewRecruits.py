# BOJ 1946 강다인
import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 갯수
result = []
for t in range(T):
    N = int(input()) # 사람 수
    n_list = [] # 점수 저장 리스트
    count = 1 # 선발 인원 count

    # 리스트에 점수 append
    for person in range(N):
        m, s = map(int, input().split()) # m = 면접 점수, s = 서류 점수
        n_list.append([m, s])

    # 면접 점수 기준 정렬
    n_list = sorted(n_list, key=lambda x:x[0]) 
    least = n_list[0][1]
    for man in range(1, N): # 현재 가리키는 사람 인덱스
        if least > n_list[man][1]:
            least = n_list[man][1]
            count += 1

    print(count)