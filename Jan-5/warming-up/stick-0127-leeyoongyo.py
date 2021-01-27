#BOJ 1094 막대기 이윤교

x = int(input())
cnt = 0
#이진법으로 나타냈을때 1의 갯수 구하기
while x:
    if x % 2 == 1: #길이가 제곱 수 이면
        cnt += 1
    x //= 2
print(cnt)


