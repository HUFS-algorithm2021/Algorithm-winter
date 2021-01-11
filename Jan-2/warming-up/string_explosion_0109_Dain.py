# # 백준 9935 강다인

Ex = input()
c4 = input()

str_stack = [] # 문자열 분해할 스택
count = -1 # 현재 스택의 index

for i in Ex:
    count += 1
    str_stack.append(i) # 스택에 문자열 추가
    if i == c4[-1]: # 마지막 폭발 문자열의 character가 현재 문자와 같을 때
        # print(str_stack[count - len(c4) + 1:count+1])
        if ''.join(str_stack[count - len(c4) + 1:count+1]) == c4: # 범위의 문자열이 폭발 문자열과 같으면
            del str_stack[count - len(c4) + 1:count+1] # 스택에서 삭제
            count -= len(c4) # 인덱스 감소

if len(str_stack) == 0:
    print("FRULA")
else:
    print(''.join(str_stack))

