# 백준 18238 임나경

string = input()
standard = "A" # 기준
time = 0 # 시간

tmp = ord(string[0]) - 65
if tmp <= 13:
    time += tmp
else:
    time += 65 - (ord(string[0]) - 26)
standard = string[0]

for i in range(len(string)-1):
    tmp = abs(ord(string[i+1]) - ord(string[i]))
    if tmp <= 13:
        time += tmp
    elif ord(string[i]) < ord(string[i+1]):
        time += ord(string[i]) - ord(string[i+1]) + 26
    else:
        time += ord(string[i+1]) - ord(string[i]) + 26
    standard = string[i+1]

print(time)