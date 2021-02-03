#BOJ 10814 나이순정렬 (leeyoongyo)
import sys
input = sys.stdin.readline
n = int(input()) #온라인 저지 회원의 수 N
member=[-1]*n #-1로 초기화한 상태로 member배열 만들기
for i in range(n): #회원수만큼
    member[i] = list(input().split()) # member에 회원의 나이와 이름이 공백으로 구분되어 입력받기
member.sort(key=lambda x:int(x[0])) #나이순으로 정
for i in member:
    print(i[0],i[1]) #한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력
