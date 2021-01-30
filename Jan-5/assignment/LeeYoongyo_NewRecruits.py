#BOJ 1946번 신입사원 이윤교

import sys
input = sys.stdin.readline
t = int(input()) #테스트 케이스 개수
for _ in range(t):
    n = int(input()) #지원자의 수
    report = sorted([list(map(int,input().split())) for _ in range(n)],key = lambda x : x[0]) #n명의 서류심사성적과 면접 성적을 순서대로 리스트형식으로 입력받되 서류심사성적기준으로 오름차순정렬
    cnt = 1 #신입사원으로 선발될 수 있는 지원자 세기
    min = report[0][1] #면접 시험 성적 중 가장 좋은 성적을 찾기위함 -> 첫번째 지원자의 면접시험 성적 기준
    for _ in range(1,n):
        if report[_][1] < min: #min의 면접시험성적 보다 크면
            min = report[_][1] #신입사원으로 선발될 수 있음. -> 기준변경
            cnt += 1 #신입사원 선발자 1명추가
    print(cnt)