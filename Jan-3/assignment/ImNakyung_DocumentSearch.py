# 백준 1543 임나경

doc = input() # 문서
word = input() # 검색할 단어
count = 0
tmp = ''
for i in doc:
    tmp += i # tmp에 i를 하나씩 더함
    if tmp.find(word) != -1: # tmp에 word가 있으면
        count += 1 # count 1 증가
        tmp = '' # tmp 초기화
    else: pass
print(count) # 몇 번 등장하는지 출력