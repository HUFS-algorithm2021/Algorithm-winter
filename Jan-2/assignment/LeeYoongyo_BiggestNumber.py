#프로그래머스 가장큰수 yoongyo

numbers = list(map(str, input().split())) #숫자입력/str
answer = sorted(numbers,key = lambda x: (x[0],x[1%len(x)],x[2%len(x)],x[3%len(x)]),reverse=True) #sorting / 원소는 0이승 1000이하
s = "".join(map(str, answer)) #문자열로 전환
if int(s) == 0: #입력된 숫자가 모두 0으로 이루어져있으면
    print('0') #0 출력
else:
    print(s)
# def solution(numbers):
#     num = list(map(str, numbers))
#     answer = sorted(num,key = lambda x: (x[0],x[1%len(x)],x[2%len(x)],x[3%len(x)]),reverse=True) #sorting
#
#     s = "".join(map(str, answer)) #문자열로 전환
#     if int(s) == 0: #입력된 숫자가 모두 0으로 이루어져있으면
#         return '0' #0 출력
#     else:
#         return s