#백준 18238
s = input() #알파벳 대문자로 구성된 문자열 입력
seq_s = [0] * len(s)
time = 0 #문자열을 출력하는데 걸리는 시간

std = 0 # A 기준

for i in range(len(s)):
    seq_s[i] = ord(s[i]) - 65 #알파벳을 0부터 25까지 지정

for i in range(len(s)):
    if abs(std - seq_s[i]) < 26 - abs(std - seq_s[i]):
        time += abs(std - seq_s[i])
    else:
        time += 26 - abs(std - seq_s[i])
    std = seq_s[i]

print(time)
