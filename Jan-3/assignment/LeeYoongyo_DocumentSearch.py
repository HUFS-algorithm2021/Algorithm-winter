#BOJ 1543번 문서검색 yoongyo

doc = input()
word = input()

index = 0
cnt = 0

while len(doc) - index >= len(word):
    if doc[index:index + len(word)] == word: # index부터 word의 길이만큼 문자열과 단어가 같으면
        cnt += 1 # cnt를 1증가시키고
        index += len(word) # index를 word 길이만큼 증가시킴.
    else: #그렇지 않으면
        index += 1 #index만 1 증가시킴.

print(cnt) #cnt출력

# 한줄로 끝내버리기
# print(doc.count(word)) #count() 함수가 중복되지 않게 최대 등장하는 횟수를 반환



