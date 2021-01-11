# 프로그래머스 가장 큰 수 (신지원)

def solution(numbers):
    numbers_str = list(map(str,numbers)) #문자열로 변환한 리스트
    if sum(numbers) == 0: #합이 0이라면 0출력
        return '0'
    new_nums_str = [] #새로운 리스트
    for i in numbers_str: #비교하기 위해 길이에 따라 수 조정하고 원래 길이 함께 저장
        if len(i)==1:
            new_nums_str.append((1,i*4))
        elif len(i)==2:
            new_nums_str.append((2,i*2))
        elif len(i)==3:
            new_nums_str.append((3,i+i[0]))
        else:
            new_nums_str.append((4,i))
    new_nums_str = sorted(new_nums_str, key = lambda x:x[1],reverse = True) #수 크기에 따라 정렬
    final = ""
    for i in range(len(new_nums_str)): #정렬된 순서로 원래 길이에 따라 각 값을 문자열에 추가
        if new_nums_str[i][0] == 1:
            final += new_nums_str[i][1][0]
        elif new_nums_str[i][0] == 2:
            final += new_nums_str[i][1][:2]
        elif new_nums_str[i][0] == 3:
            final += new_nums_str[i][1][:3]
        else:
            final += new_nums_str[i][1][:4]
    return final #최종 문자열 return
    
nums = list(map(int,input().split()))
print(solution(nums))