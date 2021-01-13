#BOJ 1181 이윤교
n = int(input())
words = [input() for _ in range(n)] # 입력하는 단어를 리스트로 저장
set_words = []
sorted_words = []*n

set_words = list(set(words)) # 리스트의 중복 제거

for i in set_words:
    sorted_words.append([len(i),i]) # 단어길이와 단어를 같이 리스트로 저장

sorted_words.sort() # 길이가 짧은 것부터/길이가 같으면 사전 순으로

for i in range (len(sorted_words)):
    print(sorted_words[i][1]) #정렬된 단어들만 출력