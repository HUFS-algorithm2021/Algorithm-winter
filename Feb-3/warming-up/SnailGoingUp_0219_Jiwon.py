# 백준 2869 달팽이는 올라가고 싶다 (신지원)

A,B,V = map(int,input().split()) #A,B,V를 입력받아 각각 정수형으로 저장
move = A-B #하루에 올라갔다 내려가는 높이
days = (V-B)//move #마지막에 미끄러질 수 있는 높이 제외 며칠이 걸리는지
if (V-B)%move: #한번 더 올라가야 꼭대기를 도달할 수 있다면 (미끄러지는 것 제외)
    days += 1 #1일 추가
print(days) #며칠인지 출력