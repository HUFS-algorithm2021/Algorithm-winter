# 백준 1543 김은비 

doc = input() #첫째 줄에 문서가 주어진다
word = input() #둘째 줄에 검색하고 싶은 단어가 주어진다

print(doc.count(word)) #첫째 줄에 중복되지 않게 최대 몇 번 등장하는지 출력한다
##count함수를 사용하면 문자열에서 부분문자열의 개수를 찾을 수 있다