# 프로그래머스 가장 큰 수 임나경

def solution(arr):
    answer = ''

    arr = list(map(str, arr)) # int -> str 변환

    for i in range(len(arr)): # 입력범위가 1000이하이므로 *3을 해줌
        arr[i] *= 3

    arr.sort(reverse=True) # reverse 정렬

    for i in range(len(arr)): # 다시 /3 해주기
        if len(arr[i]) == 3:
            arr[i] = arr[i][0]
        elif len(arr[i]) == 6:
            arr[i] = arr[i][0:2]
        elif len(arr[i]) == 9:
            arr[i] = arr[i][0:3]
        else:
            arr[i] = arr[i][0:4]

    answer = answer.join(arr) # 리스트 -> 문자열 전환

    count = 0
    for i in range(len(answer)):
        if answer[i] == '0': count += 1
    if count == len(answer): answer = '0' # 모두 0이 입력된 경우 예외처리

    return answer